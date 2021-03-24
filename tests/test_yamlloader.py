# -*- coding: utf-8 -*-


from asce import load_parameter


def test_yamlloader():
    file = 'default.yml'
    v = load_parameter(file)
    print(file, v)
    assert (v['option'] == '-lA' and v['dir'] == '~')
