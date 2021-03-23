# -*- coding: utf-8 -*-


from asce import load_parameter
from pathlib import Path


PATH = Path(__file__).parents[1] / 'data/parameters'


def test_yamlloader():
    file = PATH / 'sample.yml'
    v = load_parameter(file)
    print(file, v)
    assert (v['option'] == '-lA' and v['dir'] == '~')
