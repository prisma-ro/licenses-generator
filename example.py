"""
Example for https://github.com/prisma-ro/licenses-generator/blob/main/README.md

License:
    Copyright 2021 Prisma

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from generate_licenses import Generator, Template
#           Or you can use DefaultTemplate ^^^

template = Template(
    wrapper_template='<div>\n$ctnt\n</div>',
    title_template='<h1>$ctnt</h1>\n',
    license_template='<pre>\n<code>\n$ctnt\n</code>\n</pre>'
)

generator = Generator(template, "node_modules", "licenses.txt", "\n")
# generator = Generator(DefaultTemplate(), "node_modules", "licenses.txt", "\n")
generator.write_licenses()
