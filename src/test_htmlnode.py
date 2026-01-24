import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="p", value="This is a paragraph")
        node2 = HTMLNode(tag="p", value="This is a paragraph")
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        self.assertEqual(node.children, node2.children)
        self.assertEqual(node.props, node2.props)
    def test_props(self):
        node = HTMLNode(tag="a", value="Link", href="https://www.example.com", target="_blank")
        node2 = HTMLNode(tag="a", value="Link", href="https://www.example.com", target="_blank")
        self.assertEqual(node.props, node2.props)
    def test_children(self):
        child1 = HTMLNode(tag="span", value="Child 1")
        child2 = HTMLNode(tag="span", value="Child 2")
        parent1 = HTMLNode(tag="div", children=[child1, child2])
        parent2 = HTMLNode(tag="div", children=[child1, child2])
        self.assertEqual(parent1.children, parent2.children)




if __name__ == "__main__":
    unittest.main()


