SimpleRPC
=========

SimpleRPC is a simple RPC package for Python, supporting both client
and server functions through definition of a single class.  To
implement a client and server, merely extend the ``SimpleRPC`` class
and define the RPC functions as methods of this class, decorated with
the ``@remote`` decorator.  (Note that the methods ``close()``,
``ping()``, ``connect()``, ``listen()``, and ``serve()`` are reserved,
as are the ``host``, ``port``, ``authkey``, ``mode``, and ``conn``
instance attributes and the ``connection_class`` class attribute.)  To
run the server, simply call the ``listen()`` method, which will loop
forever, accepting clients and using `eventlet`_ to spawn a thread to
serve them (implemented using the ``serve()`` method).  For the
client, simply calling the RPC method is sufficient, but the
connection can be explicitly initialized by calling the ``connect()``
method.  The connection can be closed by calling ``close()``, and a
round-trip time can be obtained by using the ``ping()`` method.  Note
that all function arguments and results must be serializable by the
Python ``json`` package.  (RPC methods may raise exceptions, as long
as the exception class is available on the client side; if it is not,
the exception will turn into an ``ImportError``.)

Note that SimpleRPC is so simple that no effort is made to use a
secure connection type, such as SSL.  For this reason, the server
should be started on 127.0.0.1, to prevent snooping.  (Clients do send
an "authkey" to the server, which the server uses to authorize the
client, but this "authkey" is sent as plain text.)  It is possible to
use a more secure connection technology, such as SSL, by extending the
``Connection`` class and setting the ``connection_class`` class
attribute of the ``SimpleRPC`` subclass to that ``Connection``
subclass.

.. _eventlet: http://eventlet.net/
