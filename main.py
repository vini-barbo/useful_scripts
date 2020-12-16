import os


class Workflow():

    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.dir = os.path.join(path, name)

    def create_git(self):
        def git_init():
            return os.system(f'cd {dir} && git init')
        git_init()

    def create_folders(self):
        sub_folders = os.path.join(self.dir, '')
        os.system(f'mkdir {dir} && mkdir {sub_folders}tests')

    def create_readme(self):
        os.system(f"cd {dir} && touch README.txt")

    def create_basics(self):
        try:
            self.create_folders()
        finally:
            self.create_git()
            self.create_readme()


class WorkflowPython(Workflow):
    def __init__(self, ver):
        super().__init__(super.path, super.name)
        self.ver = ver
        if ver is None:
            raise print('Error,please insert a python version')

    def create_pyenv(self):
        os.system(f"cd {dir} && touch '.python-version'")
        py_ver = open('.python-version', 'r')
        py_ver.write(f'{self.ver}')

    def create_env(super):
        os.system(f'cd {super.dir} && virtualenv env')

    def create_pybasics(self):
        super.create_basics()
        self.create_pyenv()
        self.create_env()


if __name__ == '__main__':
    dir = '/home/vinicius/Works/Prog/python/Tests'
    name = 'python_site'
    folders = WorkflowPython(dir, name, '3.7.9')
    print('works well')
