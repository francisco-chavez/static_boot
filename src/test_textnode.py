
import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is also a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_01(self):
        target = TextNode("Testing", TextType.PLAIN, None)
        tested = TextNode("Testing", TextType.PLAIN)
        self.assertEqual(tested, target)
    
    def test_02(self):
        node1 = TextNode("Test", TextType.PLAIN)
        node2 = TextNode("Test", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_03(self):
        node1 = TextNode("Test a", TextType.PLAIN)
        node2 = TextNode("Test b", TextType.PLAIN)
        self.assertNotEqual(node1, node2)
    


if __name__ == "__main__":
    unittest.main()
