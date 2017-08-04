from jinja2 import Template
with open('../templates/README-template.txt', 'r') as read_file:
    data = read_file.read()
    template = Template(data)
    print(template.render(title='John Doe'))

    write_file = open('output/README.md', 'w')
    write_file.write(template.render(title='John Dom'))

    write_file.close()

    read_file.close()
