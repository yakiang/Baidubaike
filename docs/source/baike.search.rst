
.. _baike.search:

Baike.search
************

By default it queries 10 results at page 1::
	
    >>> from baidubaike import Search
    >>> search = Search('google')

to get more results at other page number::

    >>> search = Search('google', results_n=20, page_n=2)
    # get 20 results at page 2

to get the results::

    >>> results = search.get_results()

    >>> for r in results:
    ...     print r['title']
    ...     print r['url']
    ...     print r['discription']



