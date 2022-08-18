import logging
import os
import pathlib
import shutil
import uuid

from typing import Optional

from mkdocs import utils
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.config.base import Config
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files, File

log = logging.getLogger('mkdocs.plugin.eggs-info')
log.addFilter(utils.warning_filter)

STATIC_RESOURCE_BASE_URI = f"assets/eggs/{str(uuid.uuid4())}"


class EggsInfoPlugin(BasePlugin):
  # Any options that this plugin supplies should go here.
  config_scheme = ()

  @staticmethod
  def on_post_build(config: Config) -> None:
    """
    The `post_build` event does not alter any variables. Use this event to call
    post-build scripts.
    Parameters:
      config: global configuration object
    """

    for sr in ['egg.js', 'egg.css']:
      dest_path = os.path.join(
        config['site_dir'], STATIC_RESOURCE_BASE_URI, 'egg.js'
      )

      os.makedirs(pathlib.Path(dest_path).parent.resolve(), exist_ok=True)

      shutil.copyfile(
        os.path.join(
          pathlib.Path(__file__).parent.resolve(),
          "static",
          sr
        ),
        os.path.join(dest_path)
      )

  @staticmethod
  def on_page_content(html: str, page: Page, config: Config, files: Files) -> Optional[str]:
    """
    The `page_content` event is called after the Markdown text is rendered to
    HTML (but before being passed to a template) and can be used to alter the
    HTML body of the page.
    Parameters:
      html: HTML rendered from Markdown source as string
      page: `mkdocs.nav.Page` instance
      config: global configuration object
      files: global files collection
    Returns:
      HTML rendered from Markdown source as string
    """

    html += f"""
    <script src="{STATIC_RESOURCE_BASE_URI}/egg.js"></script>
    """
    return html
