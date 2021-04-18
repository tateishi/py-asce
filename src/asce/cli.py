# -*- coding: utf-8 -*-


import asce
from cleo import Command, Application


class ShowCommand(Command):
    """
    ShowCommand

    show
    """

    def handle(self):
        print([str(p) for p in asce.get_path_list()])


class RunCommand(Command):
    """
    RunCommand

    run
        {--t|template=default.tmpl : template filename}
        {--p|parameter=default.yml : parameter yaml filename}
    """

    def handle(self):
        import subprocess

        template = asce.load_template(self.option('template'))
        parameter = asce.load_parameter(self.option('parameter'))
        cmd = template.render(parameter)
        cmd_lists = cmd.split()
        print(template.render(parameter))
        print(cmd_lists)
        subprocess.run(cmd_lists)


class InfoCommand(Command):
    """
    InfoCommand

    info
        {--t|template=default.tmpl : template filename}
        {--p|parameter=default.yml : parameter yaml filename}
    """

    def handle(self):
        template = asce.load_template(self.option('template'))
        parameter = asce.load_parameter(self.option('parameter'))
        print(template.render(parameter))


class PathCommand(Command):
    """
    PathCommand

    path
        {--t|template=default.tmpl : template filename}
        {--p|parameter=default.yml : parameter yaml filename}
    """

    def search_file(self, path_list, filename):
        found = False
        for path in path_list:
            file = path / filename
            if file.is_file():
                if found:
                    print(file, " - found but not used")
                else:
                    print(file, " - found")
                found = True
            else:
                print(file, " - not found")

    def handle(self):
        print('searching template file')
        (path_list, file) = asce.find_paths_file(
            asce.get_template_path_list(),
            self.option('template')
        )
        self.search_file(path_list, file)

        print()

        print('searching parameter file')
        (path_list, file) = asce.find_paths_file(
            asce.get_parameter_path_list(),
            self.option('parameter')
        )
        self.search_file(path_list, file)


def main():
    application = Application('asce', asce.__version__, complete=True)
    application.add(ShowCommand())
    application.add(RunCommand())
    application.add(InfoCommand())
    application.add(PathCommand())
    application.run()


if __name__ == '__main__':
    main()
