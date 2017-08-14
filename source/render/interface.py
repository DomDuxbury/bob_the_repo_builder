import utils
import os
import subprocess
from shutil import copyfile


def magic(file_path):
    mode = os.stat(file_path).st_mode
    mode |= (mode & 0o444) >> 2
    os.chmod(file_path, mode)


def run_install_script(set_up):
    install_output = set_up['name'] + '/' + 'install.sh'
    create_install_script(set_up, install_output)
    magic(install_output)
    os.chdir(set_up['name'])
    subprocess.call('./install.sh', shell=True)


def create_install_script(set_up, install_output):
    install_loc = './render/templates/install-template.txt'
    utils.render(install_loc, install_output, set_up)


def create_repo(set_up):
    template_folder = './render/templates/'
    if set_up['readme']:
        readme_output = set_up['name'] + '/' + 'README.md'
        readme_loc = template_folder + 'README-template.txt'
        utils.render(readme_loc, readme_output, set_up)

    if set_up['hooks']:
        precommit_template = './render/templates/pre-commit-template.txt'
        precommit_output = set_up['name'] + '/' + 'pre-commit.sh'
        copyfile(precommit_template, precommit_output)
        magic(precommit_output)

    run_install_script(set_up)
