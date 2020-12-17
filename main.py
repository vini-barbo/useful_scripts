import os


class Workflow():

    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.dir = os.path.join(path, name)
        self.sub_dir = os.path.join(self.dir, '')
        print(f'--------------{self.dir}---------------')

    def create_git(self):
        def git_init():
            return os.system(f'cd {dir} && git init')
        git_init()

    def create_folders(self):
        print(f'--------------{self.sub_dir}---------------')
        os.system(f'mkdir {self.dir} && mkdir {self.sub_dir}tests')

    def create_readme(self):
        os.system(f"touch {self.sub_dir}README.txt")

    def create_basics(self):
        try:
            self.create_folders()
        finally:
            self.create_git()
            self.create_readme()


class WorkflowPython(Workflow):
    def __init__(self, path, name, ver):
        super().__init__(path, name)
        self.ver = ver
        if ver is None:
            raise print('Error,please insert a python version')

    def create_pyenv(self):
        os.system(f"touch {self.sub_dir}.python-version")
        py_ver = open(f'{self.sub_dir}.python-version', 'w')
        py_ver.write(f'{self.ver}')
        py_ver.close()

    def create_env(self):
        os.system(f'virtualenv {self.sub_dir}env')

    def create_pybasics(self):
        self.create_basics()
        self.create_pyenv()
        self.create_env()


if __name__ == '__main__':
    dir = '/home/vinicius/Works/Prog/python/Tests'
    name = 'python_site'
    folders = WorkflowPython(dir, name, '3.7.9')
    folders.create_pybasics()
    print('works well')
