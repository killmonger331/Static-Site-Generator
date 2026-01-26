from textnode import TextNode, TextType, BlockType
import re


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        for alt, url in images:
            before, remaining_text = remaining_text.split(
                f"![{alt}]({url})", 1
            )

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        for text, url in links:
            before, remaining_text = remaining_text.split(
                f"[{text}]({url})", 1
            )

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(text, TextType.LINK, url))

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    return [TextNode(text, TextType.TEXT)]

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        stripped = block.strip()
        if stripped:
            cleaned_blocks.append(stripped)
    return cleaned_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    # Heading: 1–6 #'s followed by a space
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING

    # Code block: must start and end with ```
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Quote: every line starts with "> "
    if all(line.startswith("> ") for line in lines):
        return BlockType.QUOTE

    # Unordered list: every line starts with "- "
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list: lines start with 1., 2., 3., ...
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            break
    else:
        return BlockType.ORDERED_LIST

    # Default
    return BlockType.PARAGRAPH

