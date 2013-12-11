from distutils.core import setup

dependencies = [
    "beautifulsoup4", 
    "requests"
]

setup(
    name = 'baidubaike',
    packages = ['baidubaike'], 
    version = '1.0',
    description = 'A wrapper of Baidu Baike',
    author = 'yakiang',
    author_email = 'strak47@gmail.com',
    url = 'https://github.com/yakiang/baidubaike',   
    download_url = 'http://yakiang.com/project/baidubaike-1.0.tar.gz', 
    keywords = ['baidu', 'wiki', 'API', 'html'], 
    classifiers = (
        'Operating System :: OS Independent', 
        'Development Status :: 4 - Beta', 
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content', 
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ), 
    long_description = """
    test
    """
)
