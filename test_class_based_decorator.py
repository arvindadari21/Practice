"""
Testing class based decorator
"""


import unittest
from class_based_decorators import CustomClassBasedDecorator


def testfunc():
    print("This is the test-function")


class TestClassBasedDecorators(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_class_based_decorator(self):
        # TODO: test class based decorators
        print("** Testing custom class based decorator **")
        CustomClassBasedDecorator()(testfunc)()
