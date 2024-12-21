import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_raises_value_error_if_has_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [])
            node.to_html()

    def test_raises_value_error_if_has_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("div", None)
            node.to_html()

    def test_creates_a_nested_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual("<div><span><b>grandchild</b></span></div>", parent_node.to_html())

if __name__ == "__main__":
    unittest.main()