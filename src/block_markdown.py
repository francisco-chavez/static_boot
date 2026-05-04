
import re 

from enum import Enum 
from textnode import TextNode, TextType


BlockType = Enum("BlockType", [ "paragraph", "heading", "code", "quote", "unordered_list", "ordered_list" ])

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    blocks = [ section.strip() for section in blocks ]
    blocks = [ block for block in blocks if block != "" ]
    return blocks

def block_to_block_type(markdown_block):
    if re.match("#{1,6} ", markdown_block) is not None:
        return BlockType.heading
    
    lines = markdown_block.split('\n')
    if len(lines) > 1 and "```" == lines[0] and lines[-1].endswith("```"):
        return BlockType.code
    
    if all(re.match(">", line) is not None for line in lines):
        return BlockType.quote
    
    if all(re.match("- ", line) is not None for line in lines):
        return BlockType.unordered_list

    if all(re.match(f"{i + 1}. ", lines[i]) is not None for i in range(0, len(lines))):
        return BlockType.ordered_list

    return BlockType.paragraph
