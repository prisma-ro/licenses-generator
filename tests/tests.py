"""
Tests for https://github.com/prisma-ro/licenses-generator

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

import unittest
from generate_licenses import Generator

INITIAL_DIR = "tests/test_initial_dir"


class TestGeneratorMethods(unittest.TestCase):
    def test_is_license(self) -> None:
        valid_license_names = [
            "LICENSE",
            "license",
            "License",
            "LICENSE.md",
            "license.md",
            "License.md",
            "LICENSE.txt",
            "license.txt",
            "License.txt",
        ]
        invalid_license_names = [
            "README",
            "readme.md",
            "readme.txt",
        ]

        for license_name in valid_license_names:
            self.assertEqual(Generator.is_license(license_name), True)

        for license_name in invalid_license_names:
            self.assertEqual(Generator.is_license(license_name), False)

    def test_find_licenses(self) -> None:
        found_licenses1 = Generator.find_licenses(INITIAL_DIR)
        found_licenses2 = Generator.find_licenses(f'{INITIAL_DIR}/')

        self.assertEqual(len(found_licenses1), len(found_licenses2))
        self.assertEqual(len(found_licenses1), 3)

        correct_paths = [
            f'{INITIAL_DIR}/LICENSE',
            f'{INITIAL_DIR}/package/license',
            f'{INITIAL_DIR}/package/nested_package/License',
        ]

        for i in range(len(found_licenses2)):
            _path = found_licenses2[i].path.replace("\\", "/")
            self.assertEqual(_path, correct_paths[i])


if __name__ == "__main__":
    unittest.main()
