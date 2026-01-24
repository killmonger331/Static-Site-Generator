import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(value="Just some text")
        self.assertEqual(node.to_html(), "Just some text")
    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click here", href="https://www.example.com", target="_blank")
        self.assertEqual(node.to_html(), '<a href="https://www.example.com" target="_blank">Click here</a>')

if __name__ == "__main__":
    unittest.main()


