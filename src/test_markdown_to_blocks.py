import unittest
from inline_markdown import extract_markdown_images, split_nodes_image, split_nodes_link, markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_excessive_newlines(self):
        md = """

This is a paragraph



This is another paragraph


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph",
                "This is another paragraph",
            ],
        )

    def test_single_block(self):
        md = "Just a single block with no newlines"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["Just a single block with no newlines"],
        )

    def test_leading_and_trailing_whitespace(self):
        md = "   \n\n  Block with whitespace   \n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["Block with whitespace"],
        )

    def test_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])


if __name__ == "__main__":
    unittest.main()
