"""
This type stub file was generated by pyright.
"""

import werkzeug.test
from contextlib import contextmanager
from click.testing import CliRunner
from werkzeug.test import Client

"""
This type stub file was generated by pyright.
"""
class EnvironBuilder(werkzeug.test.EnvironBuilder):
    """An :class:`~werkzeug.test.EnvironBuilder`, that takes defaults from the
    application.

    :param app: The Flask application to configure the environment from.
    :param path: URL path being requested.
    :param base_url: Base URL where the app is being served, which
        ``path`` is relative to. If not given, built from
        :data:`PREFERRED_URL_SCHEME`, ``subdomain``,
        :data:`SERVER_NAME`, and :data:`APPLICATION_ROOT`.
    :param subdomain: Subdomain name to append to :data:`SERVER_NAME`.
    :param url_scheme: Scheme to use instead of
        :data:`PREFERRED_URL_SCHEME`.
    :param json: If given, this is serialized as JSON and passed as
        ``data``. Also defaults ``content_type`` to
        ``application/json``.
    :param args: other positional arguments passed to
        :class:`~werkzeug.test.EnvironBuilder`.
    :param kwargs: other keyword arguments passed to
        :class:`~werkzeug.test.EnvironBuilder`.
    """
    def __init__(self, app, path=..., base_url=..., subdomain=..., url_scheme=..., *args, **kwargs) -> None:
        ...
    
    def json_dumps(self, obj, **kwargs):
        """Serialize ``obj`` to a JSON-formatted string.

        The serialization will be configured according to the config associated
        with this EnvironBuilder's ``app``.
        """
        ...
    


def make_test_environ_builder(*args, **kwargs):
    """Create a :class:`flask.testing.EnvironBuilder`.

    .. deprecated: 1.1
        Will be removed in 2.0. Construct
        ``flask.testing.EnvironBuilder`` directly instead.
    """
    ...

class FlaskClient(Client):
    """Works like a regular Werkzeug test client but has some knowledge about
    how Flask works to defer the cleanup of the request context stack to the
    end of a ``with`` body when used in a ``with`` statement.  For general
    information about how to use this class refer to
    :class:`werkzeug.test.Client`.

    .. versionchanged:: 0.12
       `app.test_client()` includes preset default environment, which can be
       set after instantiation of the `app.test_client()` object in
       `client.environ_base`.

    Basic usage is outlined in the :ref:`testing` chapter.
    """
    preserve_context = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @contextmanager
    def session_transaction(self, *args, **kwargs):
        """When used in combination with a ``with`` statement this opens a
        session transaction.  This can be used to modify the session that
        the test client uses.  Once the ``with`` block is left the session is
        stored back.

        ::

            with client.session_transaction() as session:
                session['value'] = 42

        Internally this is implemented by going through a temporary test
        request context and since session handling could depend on
        request variables this function accepts the same arguments as
        :meth:`~flask.Flask.test_request_context` which are directly
        passed through.
        """
        ...
    
    def open(self, *args, **kwargs):
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, exc_type, exc_value, tb):
        ...
    


class FlaskCliRunner(CliRunner):
    """A :class:`~click.testing.CliRunner` for testing a Flask app's
    CLI commands. Typically created using
    :meth:`~flask.Flask.test_cli_runner`. See :ref:`testing-cli`.
    """
    def __init__(self, app, **kwargs) -> None:
        ...
    
    def invoke(self, cli=..., args=..., **kwargs):
        """Invokes a CLI command in an isolated environment. See
        :meth:`CliRunner.invoke <click.testing.CliRunner.invoke>` for
        full method documentation. See :ref:`testing-cli` for examples.

        If the ``obj`` argument is not given, passes an instance of
        :class:`~flask.cli.ScriptInfo` that knows how to load the Flask
        app being tested.

        :param cli: Command object to invoke. Default is the app's
            :attr:`~flask.app.Flask.cli` group.
        :param args: List of strings to invoke the command with.

        :return: a :class:`~click.testing.Result` object.
        """
        ...
    


