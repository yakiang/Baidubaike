#-*-coding:utf-8-*-
from distutils.core import setup

dependencies = [
    "beautifulsoup4", 
    "requests"
]

setup(
    name = 'baidubaike',
    packages = ['baidubaike'], 
    version = '1.3.0',
    description = 'A wrapper of Baidu Baike',
    author = 'yakiang',
    author_email = 'strak47@gmail.com',
    url = 'https://github.com/yakiang/baidubaike',   
    download_url = 'http://yakiang.com/projects/baidubaike.tar.gz', 
    keywords = ['baidu', 'wiki', 'API', 'html'], 
    classifiers = (
        'Natural Language :: Chinese (Simplified)', 
        'Natural Language :: Chinese (Traditional)', 
        'Operating System :: OS Independent', 
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content', 
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ), 
    long_description = """

    With this package you can easily get content of an item in Baidu Baike,
    you can also search relative items. 

    百度百科词条内容的简单封装，可轻松获取词条内容、内部链接、词条标签、参考链接等，
    亦可搜索词条关键词获取结果。

    """
)
