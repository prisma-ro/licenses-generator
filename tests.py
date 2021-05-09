import unittest
from generate_licenses import Generator


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
        found_licenses1 = Generator.find_licenses('test/')
        found_licenses2 = Generator.find_licenses('test')

        self.assertEqual(len(found_licenses1), len(found_licenses2))
        self.assertEqual(len(found_licenses1), 3)

        correct_paths = [
            'test/LICENSE',
            'test/package/license',
            'test/package/nested_package/License',
        ]

        for i in range(len(found_licenses2)):
            _path = found_licenses2[i].path.replace("\\", "/")
            self.assertEqual(_path, correct_paths[i])


if __name__ == "__main__":
    unittest.main()
