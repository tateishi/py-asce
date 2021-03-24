# -*- coding: utf-8 -*-


import asce
from pathlib import Path


DATA_PATH = Path.cwd() / 'data'
TEMPLATE_PATH = [
    DATA_PATH / 'templates',
]
PARAMETER_PATH = DATA_PATH / 'parameters'


def main():
    print("Hello, world")
    print(DATA_PATH)
    template = asce.load_template(TEMPLATE_PATH, 'sample.txt')
    parameter = asce.load_parameter(PARAMETER_PATH / 'sample.yml')
    print(template.render(parameter))


if __name__ == '__main__':
    main()
