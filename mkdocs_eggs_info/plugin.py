import logging
import os
import posixpath
import textwrap

from mkdocs import utils
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

log = logging.getLogger('mkdocs.plugin.eggs-info')
log.addFilter(utils.warning_filter)


class EggsInfoPlugin(BasePlugin):
  # Any options that this plugin supplies should go here.
  config_scheme = ()