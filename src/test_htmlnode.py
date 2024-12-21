import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_returns_empty_string_with_no_props(self):
        node = HTMLNode()
        self.assertEqual("", node.props_to_html())

    def test_raises_value_error_with_not_a_dictionary_instance(self):
        with self.assertRaises(ValueError):
            node = HTMLNode(props="not a dict")
            node.props_to_html()

    def test_returns_correct_props_with_dictionary(self):
        props = {
                "href": "https://www.google.com", 
                "target": "_blank",
        }

        node = HTMLNode(props=props)
        self.assertEqual(" href=\"https://www.google.com\" target=\"_blank\"", node.props_to_html())    


if __name__ == "__main__":
    unittest.main()