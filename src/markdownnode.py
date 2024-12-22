from helpers import *
from parentnode import ParentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    children = []
    for block in blocks:
        node = block_to_node(block)
        children.append(node)
    
    return ParentNode("div", children=children)

def block_to_node(block):
    block_type = block_to_block_type(block)

    match(block_type):
        case "paragraph":
            return paragraph_to_node(block)
        case "unordered_list":
            return ulist_to_html_node(block)
        case "ordered_list":
            return olist_to_html_node(block)
        case "heading":
            return heading_to_html_node(block)
        case "quote":
            return quote_to_html_node(block)
        case "code":
            return code_to_html_node(block)
        
    raise ValueError("Invalid block type")

        
def paragraph_to_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)

    return ParentNode("p", children=children)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))

    return ParentNode("ul", html_items)

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))

    return ParentNode("ol", html_items)

def heading_to_html_node(block):
    parts = block.split(" ")

    return ParentNode(f"h{len(parts[0])}", children=text_to_children(" ".join(parts[1:])))

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def text_to_children(paragraph):
    text_nodes = text_to_text_nodes(paragraph)

    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)

    return children