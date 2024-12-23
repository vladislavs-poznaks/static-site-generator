import unittest

from contents import extract_title

class TestContents(unittest.TestCase):
    def test_extracts_title(self):
        md = """
# Test title

Paragraph

"""

        title = extract_title(md)
        self.assertEqual("Test title", title)

    def test_extracts_the_level_one_title(self):
        md = """
### Test title1

    
    
    # Test title 



Paragraph

"""

        title = extract_title(md)
        self.assertEqual("Test title", title)

    def test_raises_exception(self):
        md = """
Paragraph

"""
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()