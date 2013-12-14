Baidubaike
##########

**baidubaike** 是一个百度百科的简单封装，可轻松抓取词条内容、获取标签、内部链接等，亦可输入关键词获取词条搜索结果。

**baidubaike** is a simple wrapper of the site BaiduBaike. With it you can easily scratch contents, tags, inside urls and so on. Searching for relative results is also supported.


Installation
============

::

    $ pip install baidubaike


Requirements  
""""""""""""

+ requests
+ beautifulsoup4


Examples
========

.. code:: python

    >>> from baidubaike import Page
    >>> google = Page('google')
    >>> google.get_info()
    # {'url': u'http://baike.baidu.com/view/105.htm',  'last_modify_time': u'2013-12-04',  'title': u'google'}


More usage at `Readthedocs <http://baidubaike.readthedocs.org/en/latest/>`_


License
=======
`MIT Licensed. <https://github.com/yakiang/Baidubaike/blob/master/LICENSE>`_


Thanks to
=========

* `goldsmith/Wikipedia <https://github.com/goldsmith/Wikipedia>`_
* `百度百科 <http://baike.baidu.com>`_


