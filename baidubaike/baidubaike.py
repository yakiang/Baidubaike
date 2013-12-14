#-*-coding:utf-8-*- 

import re
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

from exception import *


CLASS_DISAMBIGUATION = ['nslog:519']
CLASS_CREATOR        = ['nslog:1022']
CLASS_REFERENCE      = ['nslog:1968']
CLASS_TAG            = ['nslog:7336', 'taglist']
CLASS_CONTENT        = ['lemmaTitleH1', 'headline-1', 'headline-2', 'para']



class Page(object):

    def __init__(self, string, encoding='utf-8'):

        url = 'http://baike.baidu.com/search/word'
        payload = None

        # An url or a word to be Paged
        pattern = re.compile('^http:\/\/baike\.baidu\.com\/.*', re.IGNORECASE)
        if re.match(pattern, string):
            url = string
        else:
            payload = {'pic':1, 'enc':encoding, 'word':string}

        self.http = requests.get(url, params=payload)
        self.html = self.http.content
        self.soup = BeautifulSoup(self.html)

        # Exceptions
        if self.soup.find(class_=CLASS_DISAMBIGUATION):
            raise DisambiguationError(string.decode('utf-8'), self.get_inurls())
        if '百度百科尚未收录词条' in self.html:
            raise PageError(string)
        if self.soup.find(id='vf'):
            raise VerifyError(string)


    def get_info(self):
        """ Get informations of the page """

        info = {}
        title = self.soup.title.get_text()
        info['title'] = title[:title.rfind('_')]
        info['url'] = self.http.url

        try:
            info['page_view'] = self.group.find(id='viewPV').get_text()
            info['last_modify_time'] = self.soup.find(id='lastModifyTime').get_text()
            info['creator'] = self.soup.find(class_=CLASS_CREATOR).get_text()

        finally:
            return info

    
    def get_content(self):
        """ Get main content of a page """

        content_list = self.soup.find_all(class_=CLASS_CONTENT)
        content = []

        for text in content_list:
            if CLASS_CONTENT[0] in text.get('class'):
                content.append('==== %s ====\n\n'%text.get_text())
            elif CLASS_CONTENT[1] in text.get('class'):
                content.append('\n== %s ==\n'%text.get_text())
            elif CLASS_CONTENT[2] in text.get('class'):
                content.append('\n* %s *\n'%text.get_text())
            elif CLASS_CONTENT[3] in text.get('class'):
                content.append('%s'%text.get_text())

        return '\n'.join(content)


    def get_inurls(self):
        """ Get links inside a page """

        inurls = OrderedDict() 
        href = self.soup.find_all(href=re.compile('\/(sub)?view(\/[0-9]*)+.htm'))

        for url in href:
            inurls[url.get_text()] = 'http://baike.baidu.com%s'%url.get('href')

        return inurls


    def get_tags(self):
        """ Get tags of the page """

        tags = []
        for tag in self.soup.find_all(class_=CLASS_TAG):
            tags.append(tag.get_text())

        return tags

    
    def get_references(self):
        """ Get references of the page """

        references = []

        for ref in self.soup.find_all(class_=CLASS_REFERENCE):
            r = {}
            r['title'] = ref.get_text()
            r['url'] = ref.get('href')
            references.append(r)

        return references



class Search(object):

    def __init__(self, word, results_n=10, page_n=1):
        
        # Generate searching URL
        url = 'http://baike.baidu.com/search'
        pn = (page_n - 1) * results_n
        payload = {'type':0, 'submit':'search', 'pn':pn, 'rn':results_n, 'word':word}

        self.http = requests.get(url, params=payload)
        self.html = self.http.content
        self.soup = BeautifulSoup(self.html)


    def get_results(self):
        """ Get searching results """

        search_results = []
        items = self.soup.find_all(class_='f')      # get results items

        for item in items:
            result = {}
            a = item.find('a')                      
            title = a.get_text()                    # get result title
            title = title[:title.rfind('_')]
            result['title'] = title
            result['url'] = a.get('href')           # get result links
            # get result discription
            result['discription'] = item.find(class_='abstract').get_text().strip()
            search_results.append(result)

        return search_results
