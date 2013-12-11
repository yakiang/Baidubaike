Baidubaike
##########

**baidubaike** 是一个百度百科词条内容的简单封装。


Installation
============

::

    $ pip install baidubaike


Examples
========

.. code:: python

    >>> from baidubaike import Page
    >>> google = Page('google')
    >>> google.get_info()
    # {'url': u'http://baike.baidu.com/view/105.htm',  'last_modify_time': u'2013-12-04',  'title': u'google'}


License
=======
`MIT Licensed. <https://github.com/yakiang/Baidubaike/blob/master/LICENSE>`_


Thanks to
=========

* `goldsmith/Wikipedia <https://github.com/goldsmith/Wikipedia>`_
* `百度百科 <http://baike.baidu.com>`_


