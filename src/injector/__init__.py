# -*- coding: utf-8 -*-

from injector import (
    any,
    payload,
)


def injector_from_payload(payload_name, **kw):

    return generate_injector(payload.get_payload(payload_name), **kw)


def generate_injector(inj_payload, as_name='payload', allow_parent_passing=False):

    def injector(func):

        def wrapper(*args, **kw):

            func_g = func.__globals__
            sentinel = object()

            parent_name = 'parent_{}'.format(as_name)
            parent_prev_g = func_g.get(parent_name, sentinel)

            if allow_parent_passing and parent_name in kw:
                parent_g = kw.pop(parent_name, None)
                func_g[parent_name] = parent_g

            prev_g = func_g.get(as_name, sentinel)
            func_g[as_name] = inj_payload

            try:
                res = func(*args, **kw)
            finally:
                if prev_g is sentinel:
                    del func_g[as_name]
                else:
                    func_g[as_name] = prev_g

                if allow_parent_passing and parent_name in func_g:
                    if parent_prev_g is sentinel:
                        func_g[parent_name] = None
                    else:
                        func_g[parent_name] = parent_prev_g

            return res

        return wrapper

    return injector

