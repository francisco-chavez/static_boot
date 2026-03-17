
import re 

from textnode import TextNode, TextType

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    results = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            results.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        results.extend(split_nodes)
    return results


def split_nodes_image(old_nodes):
    return split_nodes(old_nodes, extract_markdown_images, TextType.IMAGE, lambda x: f"![{x[0]}]({x[1]})")

def split_nodes_link(old_nodes):
    return split_nodes(old_nodes, extract_markdown_links, TextType.LINK, lambda x: f"[{x[0]}]({x[1]})")


def extract_markdown_images(text):
   return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes(old_nodes, extraction_function, text_type, combination_function):
    new_nodes = []
    for node in old_nodes:
        current_text = node.text
        targets_found = extraction_function(current_text)
        if len(targets_found) == 0:
            new_nodes.append(node)
            continue
        for target in targets_found:
            sections = current_text.split(combination_function(target), 1)
            if sections[0] != '':
                new_node = TextNode(text = sections[0], text_type = TextType.TEXT)
                new_nodes.append(new_node)
            new_node = TextNode(text = target[0], text_type=text_type, url=target[1])
            new_nodes.append(new_node)
            current_text = sections[1]
        if current_text != '':
            new_node = TextNode(text = current_text, text_type=TextType.TEXT)
            new_nodes.append(new_node)
    return new_nodes

