import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode, ParentNode

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "strong")
        self.assertEqual(html_node.value, "This is bold text")
    def test_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "em")
        self.assertEqual(html_node.value, "This is italic text")

if __name__ == "__main__":
    unittest.main()