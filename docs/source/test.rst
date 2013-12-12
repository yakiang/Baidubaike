
.. _quickstart:

Quickstart
**********

Start using wikipedia for Python in less than 5 minutes! If you are looking for the the full developer API, see :ref:`api`.

Begin by installing wikipedia::

	$ pip install wikipedia

Now let's use search and suggestion.

As you might guess, 
``wikipedia.search`` does a Wikipedia search for a query, 
and ``wikipedia.suggest`` returns the suggested Wikipedia title for a query, or ``None``::
	
    >>> from baidubaike import Page
    >>> page = Page('google')

    >>> info = page.get_info()
    # returns some basic information about the page as a dict
    >>> print info['title'], info['url']
    >>> print info.get('last_modify_time'), info.get('creator')
    # these two keys may not be included

    >>> page.get_content()
    # returns main content of the page as a string

    >>> links = page.get_inurls()
    # returns urls that refer to other pages as an OrderedDict
    >>> for word in links:
    ...     print word, links[word]

    >>> page.get_tags()
    # returns a list of relative tags

    >>> ref = page.get_references()
    # returns a list of reference links
    >>> for r in ref:
    ...     print r['title']
    ...     print r['url']

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
