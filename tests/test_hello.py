# -*- coding: utf-8 -*-

from .context import hello
import HtmlTestRunner
import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        print("setup")

    def tearDown(self):
        print("tearDown")

    def test_hello(self):
        self.assertEqual(hello.hello("Python"), "Hello, Python")

    def test_exception(self):
        with self.assertRaises(ZeroDivisionError):
            3 / 0

    @unittest.skip("skip it")
    def test_i_dont_want_to_run_now(self):
        self.assertEquals(1, 2)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
