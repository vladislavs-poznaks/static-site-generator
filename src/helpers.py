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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            node_text = node.text
            for text, url in images:
                parts = node_text.split(f"![{text}]({url})")
                if len(parts[0]) > 0:
                    new_nodes.append(TextNode(parts[0], TextType.NORMAL))
                new_nodes.append(TextNode(text, TextType.IMAGE, url))
                node_text = parts[1]
            if len(node_text) > 0:
                new_nodes.append(TextNode(node_text, TextType.NORMAL))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            node_text = node.text
            for text, url in links:
                parts = node_text.split(f"[{text}]({url})")
                if len(parts[0]) > 0:
                    new_nodes.append(TextNode(parts[0], TextType.NORMAL))
                new_nodes.append(TextNode(text, TextType.LINK, url))
                node_text = parts[1]
            if len(node_text) > 0:
                new_nodes.append(TextNode(node_text, TextType.NORMAL))
    
    return new_nodes

def text_to_text_nodes(text):
    node = TextNode(text, TextType.NORMAL)

    return split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(split_nodes_link(split_nodes_image([node])), "**", TextType.BOLD), "*", TextType.ITALIC), "`", TextType.CODE)

def markdown_to_blocks(text):
    sections = text.strip("\n").strip().split("\n\n")

    return list(map(lambda x: re.sub(r" {2,}", "", x.strip()), sections))

def block_to_block_type(block):
    if re.fullmatch(r"^#{1,6} .+$", block):
        return "heading"
    
    if re.fullmatch(r"^```[\s\S]*?```$", block):
        return "code"
    
    lines = block.split("\n")
    
    if re.fullmatch(r"^(>.*(\n|$))+", block):
        return "quote"
    
    if re.fullmatch(r"^([*-] .*(\n|$))+", block):
        return "unordered_list"
    
    result = "ordered_list"
    for i in range(len(lines)):
        if re.fullmatch(r"^(\d+\. .*(\n|$))+", lines[i]) is None:
            result = "paragraph"
        
        parts = lines[i].split(".")

        if parts[0] != f"{i + 1}":
            result = "paragraph"

    return result
    



