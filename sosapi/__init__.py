import pkg_resources
__version__ = pkg_resources.get_distribution("sosapi").version

from .client import BaseClient
