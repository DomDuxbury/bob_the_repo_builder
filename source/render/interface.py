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
    install_loc = './source/render/templates/install-template.txt'
    utils.render(install_loc, install_output, set_up)


def render_template(set_up, output_location, template_location,
                    template_folder='./source/render/templates/'):
    utils.render(output_location, output_location, set_up)


def create_repo(set_up):
    template_folder = './source/render/templates/'
    if set_up['readme']:
        render_template(set_up,
                        set_up['name'] + '/' + 'README.md',
                        template_folder + 'README-template.txt')

    if set_up['hooks']:
        precommit_template = template_folder + 'pre-commit-template.txt'
        precommit_output = set_up['name'] + '/' + 'pre-commit.sh'
        copyfile(precommit_template, precommit_output)
        magic(precommit_output)

    # make gitignore
    render_template(set_up,
                    set_up['name'] + '/' + '.gitignore',
                    template_folder + 'gitignore-template.txt')

    # make dummy test
    render_template(set_up,
                    set_up['name'] + '/tests/' + 'test_dummy.py',
                    template_folder + 'test-dummy-template.txt')

    run_install_script(set_up)
