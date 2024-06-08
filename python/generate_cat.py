#!/usr/bin/python
# -*-coding:utf-8-*-

import os
from jinja2 import Template


def generate_markdown(markdown_name, template_file, title, content):
    template_content = open(template_file, "rt").read()

    with open(markdown_name, "wt") as f:
        template = Template(template_content)
        content_render = template.render(title=title, content=content)

        f.write(content_render)


def main():
    python_dir = os.path.dirname(__file__)
    base_dir = os.path.dirname(python_dir)

    template_file = os.path.join(python_dir, "cat.jinja2")
    cat_file = os.path.join(base_dir, "cat.txt")
    cat = open(cat_file, "rt").read()
    generate_markdown("cat.md", template_file, "Cat", cat)


if __name__ == "__main__":
    main()
