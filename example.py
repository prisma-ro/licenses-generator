from generate_licenses import Generator, Template

template = Template(
    wrapper_template='<div>\n$ctnt\n</div>',
    title_template='<h1>$ctnt</h1>\n',
    license_template='<pre>\n<code>\n$ctnt\n</code>\n</pre>'
)

generator = Generator(template, "node_modules", "licenses.txt", "\n")
generator.write_licenses()
