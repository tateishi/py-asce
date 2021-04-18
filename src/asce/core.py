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
        envs = env.split(":")
        path_list = envs + path_list

    return path_list


def get_template_path_list():
    return [path / 'templates' for path in get_path_list()]


def get_parameter_path_list():
    return [path / 'parameters' for path in get_path_list()]


def find_paths_file(path_list, pathname):
    from pathlib import Path

    path = Path(pathname)
    if path.is_absolute():
        return ([path.parent], path.name)
    else:
        return (path_list, pathname)


def load_template(pathname):
    from jinja2 import Environment, FileSystemLoader

    (path_list, file) = find_paths_file(get_template_path_list(), pathname)
    env = Environment(
        loader=FileSystemLoader(path_list)
    )
    return env.get_template(file)


def inject_time_now(param):
    if 'now' not in param:
        from datetime import datetime
        now = datetime.now()
        param.update(dict(now=now))
    return param


def load_parameter(pathname):
    import yaml

    (path_list, file) = find_paths_file(get_parameter_path_list(), pathname)
    for path in path_list:
        if (path / file).is_file():
            with open(path / file, 'r') as f:
                return inject_time_now(yaml.safe_load(f))
    else:
        raise Exception
