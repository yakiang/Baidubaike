.. _Search:

Search
******

Examples::

    >>> from baidubaike import Search
    >>> search = Search('google')
    # by default it gets 10 results of the key word google at page 1
    >>> search = Search('google', results_n=20, page_n=2)
    # get 20 results at page 2

    >>> results = search.get_results()
    # returns the results as a list
    >>> for r in results:
    ...     print r['title']        # get result title
    ...     print r['url']          # get page url 
    ...     print r['discription']  # get result discription


