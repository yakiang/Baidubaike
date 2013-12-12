.. baidubaike documentation master file, created by
   sphinx-quickstart on Thu Dec 12 11:11:59 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to baidubaike's documentation!
======================================

.. toctree::
   :maxdepth: 2

Page
----

.. code:: python

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


besides, you can also create a Page with an existing url refering to it:

.. code:: python

    >>> page = Page('http://baike.baidu.com/view/105.htm')

you can set the encoding, by default it is *utf-8*:

.. code:: python

    >>> page = Page('google', encoding='gbk')



Search
------

.. code:: python

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



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

