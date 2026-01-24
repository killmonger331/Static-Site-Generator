class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, **props):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    def to_html(self):
        raise NotImplementedError()
    def props_to_html(self):
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str
    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, **props):
        super().__init__(tag=tag, value=value, children=[], **props)
    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value to convert to HTML")
        if not self.tag:
            return self.value
        props_str = self.props_to_html()
        return f'<{self.tag}{props_str}>{self.value}</{self.tag}>'
    def __repr__(self):
        return f'LeafNode(tag={self.tag}, value={self.value}, props={self.props})'