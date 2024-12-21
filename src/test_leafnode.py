import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_raises_value_error_if_has_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("s", None)
            node.to_html()

    def test_returns_value_as_text_if_has_no_tag(self):
        node = LeafNode(None, "test")
        self.assertEqual("test", node.to_html())

    def test_returns_value_wrapped_in_tags(self):
        node = LeafNode("s", "test")
        self.assertEqual("<s>test</s>", node.to_html())

if __name__ == "__main__":
    unittest.main()