import importlib.metadata

__version__ = importlib.metadata.version("example_package_subfolder")

from .main import * # noqa
