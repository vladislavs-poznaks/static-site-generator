from textnode import TextNode, TextType
from leafnode import LeafNode

import re

delimiters = {
    "*": TextType.ITALIC,
    "**": TextType.BOLD,
    "`": TextType.CODE,
}


def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            props = {"href": text_node.url}
            return LeafNode("a", text_node.text, props=props)
        case TextType.IMAGE:
            props = {"src": text_node.url, "alt": text_node.text}
            return LeafNode("img", text_node.text, props=props)
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            values = node.text.split(delimiter)
            for i in range(len(values)):
                if values[i] == "":
                    continue

                if i % 2 == 0:
                    new_nodes.append(TextNode(values[i], TextType.NORMAL))
                else:
                    new_nodes.append(TextNode(values[i], delimiters[delimiter]))

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
