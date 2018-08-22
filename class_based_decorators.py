"""
Class based decorators
"""


class CustomClassBasedDecorator(object):
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("This is the custom class based decorator")
            print("Wrapper around: ", func.__name__)
            func(*args, **kwargs)
        return wrapper
