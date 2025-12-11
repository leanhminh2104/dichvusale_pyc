"""
DichVuSale .pyc importer and helper utilities


Copyright (c) 2025 dichvusale.io.vn
Package: dichvusale_pyc
License: MIT
"""


from .loader import install as install_hook
from .util import compile_file, compile_directory


__all__ = ["install", "compile_file", "compile_directory"]


def install():
"""Convenience wrapper to install the .pyc import hook.


Usage:
import dichvusale_pyc
dichvusale_pyc.install()


or simply:
import dichvusale_pyc.loader # loader auto-installs on import too
"""
install_hook()
