"""
RenderCanvas: one canvas API, multiple backends.
"""

# ruff: noqa: F401

from ._version import __version__, version_info
from . import _coreutils
from ._events import EventType
from .base import BaseRenderCanvas, BaseLoop, BaseTimer

__all__ = [
    "BaseRenderCanvas",
    "EventType",
    "BaseLoop",
    "BaseTimer",
]