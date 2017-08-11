from jinja2 import Template


def get_template(file_path):
    with open(file_path, 'r') as f:
        file_string = f.read()
        f.close()
    return Template(file_string)


def write_output(output, output_path):
    write_file = open(output_path, 'w')
    write_file.write(output)
    write_file.close()


def render(template_path, output_path, data):
    template = get_template(template_path)
    output = template.render(data)
    write_output(output, output_path)
