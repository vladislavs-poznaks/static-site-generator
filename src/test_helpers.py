import unittest

from textnode import TextNode, TextType
from helpers import *

class TestHelpers(unittest.TestCase):
    def test_converts_normal_text_node_to_leaf_node(self):
        text_node = TextNode("test", TextType.NORMAL)

        leaf_node = text_node_to_html_node(text_node)

        self.assertEqual("test", leaf_node.to_html())

    def test_converts_bold_text_node_to_leaf_node(self):
        text_node = TextNode("test", TextType.BOLD)

        leaf_node = text_node_to_html_node(text_node)

        self.assertEqual("<b>test</b>", leaf_node.to_html())
    
    def test_converts_italic_text_node_to_leaf_node(self):
        text_node = TextNode("test", TextType.ITALIC)

        leaf_node = text_node_to_html_node(text_node)

        self.assertEqual("<i>test</i>", leaf_node.to_html())

    def test_converts_code_text_node_to_leaf_node(self):
        text_node = TextNode("test", TextType.CODE)

        leaf_node = text_node_to_html_node(text_node)

        self.assertEqual("<code>test</code>", leaf_node.to_html())
    
    def test_converts_link_text_node_to_leaf_node(self):
        text_node = TextNode("test", TextType.LINK, "www.example.com")

        leaf_node = text_node_to_html_node(text_node)

        self.assertEqual("<a href=\"www.example.com\">test</a>", leaf_node.to_html())

        
    def test_converts_image_text_node_to_leaf_node(self):
        text_node = TextNode("test", TextType.IMAGE, "www.example.com")

        leaf_node = text_node_to_html_node(text_node)

        self.assertEqual("<img src=\"www.example.com\" alt=\"test\"/>", leaf_node.to_html())


if __name__ == "__main__":
    unittest.main()