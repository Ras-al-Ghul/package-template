#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_dir(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':

    if '{{ cookiecutter.use_travis_ci }}' != 'y':
        remove_file('.travis.yml')

    if '{{ cookiecutter.use_appveyor_ci }}' != 'y':
        remove_file('appveyor.yml')

    if '{{ cookiecutter.use_read_the_docs }}' != 'y':
        remove_file('.rtd-environment.yml')
        remove_file('readthedocs.yml')

    if '{{ cookiecutter.cextern_folder }}' != 'y':
        remove_dir("cextern")
