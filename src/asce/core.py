# -*- coding: utf-8 -*-


def load_template(path, file):
    from jinja2 import Environment, FileSystemLoader

    env = Environment(
        loader=FileSystemLoader(path)
    )
    return env.get_template(file)


def load_parameter(path):
    import yaml

    with open(path, 'r') as f:
        return yaml.safe_load(f)
