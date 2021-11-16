"""
This type stub file was generated by pyright.
"""

from typing import Any
from werkzeug.local import LocalStack
from .app import Flask
from .wrappers import Request

class _FlaskLocalProxy(Flask):
    ...


_request_ctx_stack: LocalStack
_app_ctx_stack: LocalStack
current_app: _FlaskLocalProxy
request: Request
session: Any
g: Any