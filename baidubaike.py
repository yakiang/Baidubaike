#-*-coding:utf-8-*- 
import re
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from exception import *

class Page(object):
    def __init__(self, string, encoding='utf-8'):
        url = 'http://baike.baidu.com/search/word'
        payload = None
        pattern = re.compile('^http:\/\/baike\.baidu\.com\/.*', re.IGNORECASE)
        if re.match(pattern, string):
            url = string
        else:
            payload = {'pic':1, 'enc':encoding, 'word':string}
        self.http = requests.get(url, params=payload)
        self.html = self.http.content
        self.soup = BeautifulSoup(self.html)

        if self.soup.find(class_='nslog:519'):
            raise DisambiguationError(string, self.get_inurls())
        if '百度百科尚未收录词条' in self.html:
            raise PageError(string)

    def get_info(self):
        info = {}
        title = self.soup.title.get_text()
        info['title'] = title[:title.rfind('_')]
        info['url'] = self.http.url
        info['last_modify_time'] = self.soup.find(id='lastModifyTime').get_text()
        info['creator'] = self.soup.find(class_='nslog:1022').get_text()
        return info
    
    def get_content(self):
        content_list = self.soup.find_all(class_=['lemmaTitleH1', 'headline-1', 'headline-2', 'para'])
        content = []
        for text in content_list:
            if 'lemmaTitleH1' in text.get('class'):
                content.append('==== %s ====\n\n'%text.get_text())
            elif 'headline-1' in text.get('class'):
                content.append('\n== %s ==\n'%text.get_text())
            elif 'headline-2' in text.get('class'):
                content.append('\n* %s *\n'%text.get_text())
            elif 'para' in text.get('class'):
                content.append('%s'%text.get_text())
        return '\n'.join(content)

    def get_inurls(self):
        inurls = OrderedDict()
        href = self.soup.find_all(href=re.compile('\/(sub)?view(\/[0-9]*)+.htm'))
        for url in href:
            inurls[url.get_text()] = 'http://baike.baidu.com%s'%url.get('href')
        return inurls

    def get_tags(self):
        tags = []
        for tag in self.soup.find_all(class_=['nslog:7336', 'taglist']):
            tags.append(tag.get_text())
        return tags
    
    def get_references(self):
        references = OrderedDict()
        for ref in self.soup.find_all(class_='nslog:1968'):
            references[ref.get_text()] = ref.get('href')
        return references


class Search(object):
    def __init__(self, word, results_n=10, page_n=1):
        pn = (page_n - 1) * results_n
        url = 'http://baike.baidu.com/search'
        payload = {'type':0, 'submit':'search', 'pn':pn, 'rn':results_n, 'word':word}
        self.http = requests.get(url, params=payload)
        self.html = self.http.content
        self.soup = BeautifulSoup(self.html)

    def get_results(self):
        search_results = []
        items = self.soup.find_all(class_='f')
        for item in items:
            result = {}
            a = item.find('a')
            title = a.get_text()
            title = title[:title.rfind('_')]
            result[title] = {'url':a.get('href')}
            result[title]['discription'] = item.find(class_='abstract').get_text().strip()
            search_results.append(result)
        return search_results

    
p=Page('香港')
print p.get_inurls()
