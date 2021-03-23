# -*- coding: utf-8 -*-


import asce
from pathlib import Path


PATH0 = Path('/home/thkadmin/wks/python/py-asce/data')

PATH = [
    PATH0 / 'templates',
]


def main():
    print("Hello, world")
    print(PATH0)
    template = asce.load_template(PATH, 'sample.txt')
    parameter = asce.load_parameter(PATH0 / 'parameters/sample.yml')
    print(template.render(parameter))


if __name__ == '__main__':
    main()
