
.. _exceptions:

Exception
*********

PageError
"""""""""

Raised when no such a page exists.

DisambiguationError
"""""""""""""""""""

Raised when a word causes two or more results.

While throwing errors it will return some items that you may refer to.


VerifyError
""""""""""

Raised when a page needs a verifying-code.

This may be caused when you query too frequently.


Other
"""""

Raised by `requests <http://www.python-requests.org/en/latest/user/quickstart/#errors-and-exceptions>`_
