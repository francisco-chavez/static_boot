import unittest

from block_markdown import markdown_to_blocks, block_to_block_type, BlockType


class Test_Block_Markdown(unittest.TestCase):
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.quote)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)


    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        ) 
        
    def test_markdown_to_blocks_v2(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

       


- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

if __name__ == "__main__":
    unittest.main()
