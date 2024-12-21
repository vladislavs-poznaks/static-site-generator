import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("test", TextType.BOLD)
        node2 = TextNode("test", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_with_url(self):
        node = TextNode("test", TextType.BOLD, "www.example.com")
        node2 = TextNode("test", TextType.BOLD, "www.example.com")
        self.assertEqual(node, node2)

    def test_different_url(self):
        node = TextNode("test", TextType.BOLD, "www.example.com")
        node2 = TextNode("test", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_different_type(self):
        node = TextNode("test", TextType.NORMAL, "www.example.com")
        node2 = TextNode("test", TextType.BOLD, "www.example.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()