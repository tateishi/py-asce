# -*- coding: utf-8 -*-


import asce
from pathlib import Path
from cleo import Command, Application


DATA_PATH = Path.cwd() / 'data'
TEMPLATE_PATH = [
    DATA_PATH / 'templates',
]
PARAMETER_PATH = DATA_PATH / 'parameters'


class InfoCommand(Command):
    """
    InfoCommand

    info
    """

    def handle(self):
        print(DATA_PATH)
        template = asce.load_template(TEMPLATE_PATH, 'sample.txt')
        parameter = asce.load_parameter(PARAMETER_PATH / 'sample.yml')
        print(template.render(parameter))


def main():
    application = Application('asce', asce.__version__, complete=True)
    application.add(InfoCommand())
    application.run()


if __name__ == '__main__':
    main()
