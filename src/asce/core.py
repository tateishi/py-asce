# -*- coding: utf-8 -*-


def get_path_list():
    """
    優先順位
    1. 環境変数
    $ASCE_DATA/templates/
    $ASCE_DATA/parameters/

    2. カレントワーキングディレクトリ
    ./data/templates/
    ./data/parameters/

    3. ユーザホームディレクトリ
    ~/.asce/templates/
    ~/.asce/parameters/

    4. システムデフォルト
    /etc/asce/templates/
    /etc/asce/parameters/

    """

    import os
    from pathlib import Path

    path_list = [
        Path.cwd() / 'data',
        Path(os.path.expanduser("~")) / '.asce',
        Path('/etc/asce')
    ]
    env = os.getenv('ASCE_DATA')
    if env:
        path_list.insert(0, Path(env))

    return path_list


def get_template_path_list():
    return [path / 'templates' for path in get_path_list()]


def get_parameter_path_list():
    return [path / 'parameters' for path in get_path_list()]


def load_template(path, file='default.tmpl'):
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


def load_parameter(path_list, file='default.yml'):
    import yaml

    for path in path_list:
        if (path / file).is_file():
            with open(path / file, 'r') as f:
                return inject_time_now(yaml.safe_load(f))
    else:
        raise Exception
