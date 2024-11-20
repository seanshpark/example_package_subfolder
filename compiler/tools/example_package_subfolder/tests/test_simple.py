# from https://github.com/pypa/sampleproject/

import unittest

from example_package_subfolder import example
from example_package_subfolder import MyClass


class TestExample(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(example.hello('world'), 'hello world')

    def test_main(self):
        mc = MyClass()
        self.assertIsNotNone(mc)
        self.assertEqual(mc.hello, 'world')


if __name__ == '__main__':
    unittest.main()
