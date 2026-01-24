import unittest
from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_parent_to_html_div(self):
        child1 = LeafNode("p", "Paragraph 1")
        child2 = LeafNode("p", "Paragraph 2")
        parent = ParentNode("div", children=[child1, child2])
        self.assertEqual(parent.to_html(), "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>")
    def test_parent_to_html_with_props(self):
        child = LeafNode("span", "Some text")
        parent = ParentNode("div", children=[child], id="main", class_="container")
        self.assertEqual(parent.to_html(), '<div id="main" class_="container"><span>Some text</span></div>')
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
if __name__ == "__main__":
    unittest.main()