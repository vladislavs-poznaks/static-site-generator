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


    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.NORMAL
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.NORMAL),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.NORMAL
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.NORMAL),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()