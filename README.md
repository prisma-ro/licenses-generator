# licenses-generator
Generate a file containing all (locally found) licenses from your project.

<p align=center>
    <img src="https://img.shields.io/badge/version-1.1-blue" />
    <a href="https://github.com/prisma-ro/licenses-generator/actions/workflows/run_tests.yaml">
        <img src="https://github.com/prisma-ro/licenses-generator/actions/workflows/run_tests.yaml/badge.svg" />
    </a>
    <img src="https://img.shields.io/badge/license-Apache%202-blue" />
</p>

# About
This script is used in production @ Prisma to generate the required attributions
for our [license page](https://buyprisma.netlify.app/info/licente.html).

### How?
It walks the given directory and searches for license files, and after it's done,
it will write all of them to a new file, following the given template.

### Compatibility
At this time, it's only been tested on JS project (the default folder is `node_modules`), but it should be compatible with anything
 that stores licenses locally.

# Usage

## Recomanded
```py
from generate_licenses import Generator, Template # <- Or you can use DefaultTemplate

template = Template(
    wrapper_template='<div>\n$ctnt\n</div>',
    title_template='<h1>$ctnt</h1>\n',
    license_template='<pre>\n<code>\n$ctnt\n</code>\n</pre>'
)

generator = Generator(template, <initial_dir>, <out_file>, <out_separator>)
generator.write_licenses()
```

### CLI _(Not recomanded)_
See help: `generate_licenses.py -h`

---

## How does the Templating work?

Let's start with the given example (from above) - That will generate the following:
```html
<div>
<h1>PACKAGE_NAME</h1>
<pre>
<code>
LICENSE
</code>
</pre>
</div>
```

Basically you can write whatever you want, and put `$ctnt` where you want the 
actual "content" to be put

---

## Contributing Guide
If you wish to contribute to generate_licenses please see [CONTRIBUTING.md](CONTRIBUTING.md)

## Code of Conduct
Please respect our Code of Conduct. It can be found [here](CODE_OF_CONDUCT.md)

---

### Authors
  - David Pescariu - [prisma.ro.official@gmail.com](mailto:prisma.ro.official@gmail.com)

### License
```
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
```

<p align=center>
  <code>
(C) Prisma 2021 - https://buyprisma.netlify.app/
  </code>
</p>
