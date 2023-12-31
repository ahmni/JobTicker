"""
This type stub file was generated by pyright.
"""

from jinja2 import Markup, escape
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from . import json
from ._compat import json_available
from .app import Flask, Request, Response
from .blueprints import Blueprint
from .config import Config
from .ctx import after_this_request, copy_current_request_context, has_app_context, has_request_context
from .globals import _app_ctx_stack, _request_ctx_stack, current_app, g, request, session
from .helpers import flash, get_flashed_messages, get_template_attribute, make_response, safe_join, send_file, send_from_directory, stream_with_context, url_for
from .json import jsonify
from .signals import appcontext_popped, appcontext_pushed, appcontext_tearing_down, before_render_template, got_request_exception, message_flashed, request_finished, request_started, request_tearing_down, signals_available, template_rendered
from .templating import render_template, render_template_string

"""
This type stub file was generated by pyright.
"""
__version__ = ...
