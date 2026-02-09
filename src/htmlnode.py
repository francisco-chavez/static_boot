
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag 
        self.value = value 
        self.children = children
        self.props = props 

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        to_join = [f'{pair[0]}="{pair[1]}"' for pair in self.props.items()]
        return f" {' '.join(to_join)}"

    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nProps:{self.props_to_html}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag = tag, children = children, props = props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is missing.")
        if self.children is None:
            raise ValueError("Children are missing.")
        return f'<{self.tag}>{''.join(map(lambda c: c.to_html(), self.children))}</{self.tag}>'


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag = tag, value = value, props = props)

    def to_html(self):
        if self.value is None:
            raise ValueError()

        if self.tag is None:
            return self.value 
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>' 
