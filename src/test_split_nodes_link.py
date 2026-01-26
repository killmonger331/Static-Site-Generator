import unittest
from inline_markdown import extract_markdown_images, split_nodes_image, split_nodes_link

import unittest
from textnode import TextNode, TextType


class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and another [second link](https://www.test.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://www.test.com"),
            ],
            new_nodes,
        )
    def test_no_links(self):
        node = TextNode("This is text without links.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

if __name__ == "__main__":
    unittest.main()