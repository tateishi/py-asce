# -*- coding: utf-8 -*-


from asce import load_template
from pathlib import Path


PATH = [
    Path(__file__).parents[1] / 'data/templates',
]


def test_filesystemloader():
    from datetime import datetime
    now = datetime(2021, 3, 21, 10, 30)
    print(PATH)
    file = 'sample.txt'
    template = load_template(PATH, file)
    assert (template.render(option='-lA', dir='~', now=now, today="%Y%m%d")
            == 'ls -lA ~ 20210321')
