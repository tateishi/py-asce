# -*- coding: utf-8 -*-


from asce import load_template


def test_filesystemloader():
    from datetime import datetime
    now = datetime(2021, 3, 21, 10, 30)
    file = 'default.tmpl'
    template = load_template(file)
    assert (template.render(option='-lA', dir='~', now=now, today="%Y%m%d")
            == 'ls -lA ~ 20210321')
