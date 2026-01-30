
import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_01(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_02(self):
        node = HTMLNode(props = { "href": "https://hello.world", "target":"_blank" })
        output_to_test = node.props_to_html()
        split_output = output_to_test.split()
        check0 = output_to_test[0] == " "
        check1 = any(s == 'href="https://hello.world"' for s in split_output)
        check2 = any(s == 'target="_blank"' for s in split_output)
        checks = [ check0, check1, check2 ]
        any_fail_found = any(c == False for c in checks)
        self.assertNotEqual(any_fail_found, True)
    
    def test_03(self):
        node = HTMLNode(tag = "tag", value = "value", children = ["a", 'b', 'c'])
        self.assertEqual("", node.props_to_html())

if __name__ == "__main__":
    unittest.main()
