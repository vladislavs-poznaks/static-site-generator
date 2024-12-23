import os
import shutil

from markdownnode import markdown_to_html_node


def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.strip().startswith("# "):
            return line.strip()[2:]


    raise Exception("no title found")

def generate_files_recursive(from_dir, template_path, dest_dir):
    for filename in os.listdir(from_dir):
        from_path = os.path.join(from_dir, filename)
        dest_path = os.path.join(dest_dir, filename)

        if os.path.isfile(from_path) and filename.endswith(".md"):
            generate_page(from_path, template_path, dest_path.replace(".md", ".html"))
        else:
            generate_files_recursive(from_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as markdown_file:
        markdown = markdown_file.read()
        markdown_file.close()

    with open(template_path) as template_file:
        template = template_file.read()
        template_file.close()

    title = extract_title(markdown)

    content = markdown_to_html_node(markdown)

    html = template.replace("{{ Content }}", content.to_html()).replace("{{ Title }}", title)

    dest_dir_path = os.path.dirname(dest_path)

    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(html)
        file.close()
