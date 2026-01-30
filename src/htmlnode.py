
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
        