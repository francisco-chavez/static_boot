
from enum import Enum 
from htmlnode import LeafNode


class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text 
        self.text_type = text_type
        self.url = url 

    def __eq__(self, other):
        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    text = text_node.text 
    tag = None 
    props = None 
    match text_node.text_type:
        case TextType.PLAIN:
            tag = None
        case TextType.BOLD:
            tag = 'b'
        case TextType.ITALIC:
            tag = 'i'
        case TextType.CODE:
            tag = 'code'
        case TextType.LINK:
            tag = "a"
            props = { "href" : text_node.url }
        case TextType.IMAGE:
            tag = 'img'
            text = ''
            props = { "src" : text_node.url, "alt" : text_node.text }
        
    return LeafNode(tag=tag, value=text, props=props)
