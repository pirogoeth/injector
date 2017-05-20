# -*- coding: utf-8 -*-

from injector import payload


def injector_from_payload(payload_name, as_name='payload'):

    return generate_injector(payload.get_payload(payload_name), as_name=as_name)


def generate_injector(inj_payload, as_name='payload'):

    def injector(func):

        def wrapper(*args, **kw):

            func_g = func.__globals__
            sentinel = object()

            prev_g = func_g.get(as_name, sentinel)
            func_g[as_name] = inj_payload

            try:
                res = func(*args, **kw)
            finally:
                if prev_g is sentinel:
                    del func_g[as_name]
                else:
                    func_g[as_name] = prev_g

            return res

        return wrapper

    return injector

