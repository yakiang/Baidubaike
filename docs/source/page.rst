
.. _page:

Page
****

To create a page::
	
    >>> from baidubaike import Page
    >>> page = Page('google')

get the basic information about the page as a dict::

    >>> info = page.get_info()
    >>> print info['title'], info['url']

    >>> print info.get('last_modify_time')
    >>> print info.get('creator')
    >>> print info.get('page_view')
    # these keys might not be included

get the content of the page as a string::

    >>> page.get_content()

get urls refering to other pages as an OrderedDict::

    >>> links = page.get_inurls()
    >>> for word in links:
    ...     print word, links[word]

get a list of tags of the page::

    >>> page.get_tags()

get a list of reference links::

    >>> ref = page.get_references()
    >>> for r in ref:
    ...     print r['title']
    ...     print r['url']


besides, you can also create a Page with an existing url refering to it::

    >>> page = Page('http://baike.baidu.com/view/105.htm')

you can set the encoding, by default it is *utf-8*::

    >>> page = Page('google', encoding='gbk')
