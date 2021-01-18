import os

from cabinets import plugins
from cabinets.cabinet import (
    Cabinet,
    CabinetError,
    register_protocols,
    SUPPORTED_PROTOCOLS,
)
from cabinets.parser import (
    Parser,
    register_extensions,
    SUPPORTED_EXTENSIONS,
)

__all__ = [
    Cabinet,
    CabinetError,
    Parser,
    register_protocols,
    register_extensions,
    SUPPORTED_PROTOCOLS,
    SUPPORTED_EXTENSIONS,
]

PLUGIN_PATH = os.environ.get('PLUGIN_PATH', os.path.join(os.getcwd(), 'cabinets'))
if PLUGIN_PATH == os.path.dirname(__file__):
    PLUGIN_PATH = None
plugins.discover_all(custom_plugin_path=PLUGIN_PATH)


class InvalidURIError(Exception):
    pass


def from_uri(uri) -> (Cabinet, str):
    try:
        protocol, path = uri.split('://')
    except ValueError:
        raise InvalidURIError("Missing protocol identifier")
    cabinet_ = SUPPORTED_PROTOCOLS.get(protocol)
    if not cabinet_:
        raise InvalidURIError(f"Unknown protocol '{protocol}'")
    if not path:
        raise InvalidURIError("Empty resource path")
    return cabinet_, path


def read(uri, raw=False):
    cabinet_, path = from_uri(uri)
    return cabinet_.read(path, raw=raw)


def create(uri, content, raw=False):
    cabinet_, path = from_uri(uri)
    return cabinet_.create(path, content, raw=raw)


def delete(uri):
    cabinet_, path = from_uri(uri)
    return cabinet_.delete(path)
