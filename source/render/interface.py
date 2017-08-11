import utils

# {'git': False, 'venv': False, 'name': 'joezcool',
# 'flake': False, 'pytest': False}

# Create and run Bash
# Create project folder
# Create Venv
# Install flake8
# Install pytest
# Create requirements.txt
# Initialise git
# Install pytest watch
# Install precommit hooks
# Create README
# Create gitignore


def create_install_script(set_up):
    install_loc = './render/templates/install-template.txt'
    install_output = set_up['name'] + '/' + 'install.sh'
    utils.render(install_loc, install_output, set_up)


def create_repo(set_up):
    template_folder = './render/templates/'
    if set_up['readme']:
        readme_output = set_up['name'] + '/' + 'README.md'
        readme_loc = template_folder + 'README-template.txt'
        utils.render(readme_loc, readme_output, set_up)

    create_install_script(set_up)
