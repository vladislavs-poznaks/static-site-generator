from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent Node missing tag")
        
        if self.children is None:
            raise ValueError("Parent Node missing children")
        
        result = ""
        for node in self.children:
            result += node.to_html()

        return f"<{self.tag}>{result}</{self.tag}>"
