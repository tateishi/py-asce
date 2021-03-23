# -*- coding: utf-8 -*-


from jinja2 import Environment, FileSystemLoader


def load_template(path, file):
    env = Environment(
        loader=FileSystemLoader(path)
    )
    return env.get_template(file)
