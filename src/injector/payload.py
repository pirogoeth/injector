# -*- coding: utf-8 -*-

import logging


_payloads = {}
_LOG = logging.getLogger(__name__)


def get_payload(name):
    global _payloads

    return _payloads.get(name, None)


def create_payload(name, payload):
    global _payloads

    if name in _payloads:
        _LOG.warning("Overwriting global payload `%s`", name)

    _payloads.update({
        name: payload,
    })

    return payload


def remove_payload(name):
    global _payloads

    if name in _payloads:
        _LOG.debug("Removing global payload `%s`", name)
        _payloads.remove(name)
