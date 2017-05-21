# -*- coding: utf-8 -*-

__doc__ = """
Creates an object that accepts any method call, any property get/set,
or usage as a context manager.
"""


class AnyObject(object):

    def __init__(self, *args, **kw):

        pass

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_val, traceback):

        return None

    def __getitem__(self, key):

        return self

    def __setitem__(self, key, value):

        pass

    def __getattr__(self, key):

        return self

    def __setattr__(self, key, value):

        pass

    def __call__(self, *args, **kw):

        return self

