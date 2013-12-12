
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

