# -*- coding: utf-8 -*-


from asce.template import load_template
from pathlib import Path


PATH = [
    Path(__file__).parents[1] / 'data/templates',
]


def test_filesystemloader():
    print(PATH)
    file = 'sample.txt'
    template = load_template(PATH, file)
    assert template.render(option='-lA', dir='~') == 'ls -lA ~'
