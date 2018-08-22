"""
Class based decorators
"""


class CustomClassBasedDecorator(object):
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            test_list, test_dict = args, *kwargs
            print("This is the custom class based decorator")
            func(*args, **kwargs)
        return wrapper
