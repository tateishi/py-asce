# -*- coding: utf-8 -*-


def load_template(path, file):
    from jinja2 import Environment, FileSystemLoader

    env = Environment(
        loader=FileSystemLoader(path)
    )
    return env.get_template(file)


def inject_time_now(param):
    if 'now' not in param:
        from datetime import datetime
        now = datetime.now()
        param.update(dict(now=now))
    return param


def load_parameter(path):
    import yaml

    with open(path, 'r') as f:
        return inject_time_now(yaml.safe_load(f))
