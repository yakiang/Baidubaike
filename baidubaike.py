#-*-coding:utf-8-*- 
import re
import urllib2
from bs4 import BeautifulSoup
from collections import OrderedDict

def page(string, encoding='utf-8'):
    string = string.replace(' ', '%20')
    http = re.compile('^http:\/\/baike\.baidu\.com\/.*', re.IGNORECASE)
    if re.match(http, string):
        PAGE_URL = string
    else:
        PAGE_URL = 'http://baike.baidu.com/search/word?pic=1&enc=%s&word=%s'%(encoding, string)
    return BaikePage(PAGE_URL)

def search(title, results=10, page_n=1):
    title = title.replace(' ', '%20')
    pn = (page_n - 1) * results
    SEARCH_URL = 'http://baike.baidu.com/search?type=0&submit=search&pn=%d&rn=%d&word=%s'%(pn, results, title)
    return BaikeSearch(SEARCH_URL)
    
class BaikePage(object):
    def __init__(self, url):
        self.http = urllib2.urlopen(url)
        self.html = self.http.read()
        self.soup = BeautifulSoup(self.html)

    def get_info(self):
        info = {}
        title = self.soup.title.get_text()
        info['title'] = title[:title.rfind('_')]
        info['url'] = self.http.geturl()
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
        inurls = set()
        href = self.soup.find_all(href=re.compile('\/(sub)?view(\/[0-9]*)+.htm'))
        for url in href:
            inurls.add(url.get_text())
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


class BaikeSearch(object):
    def __init__(self, url):
        self.http = urllib2.urlopen(url)
        self.html = self.http.read()
        self.soup = BeautifulSoup(self.html)

    def get_results(self):
        search_results = []
        items = self.soup.find_all(class_='f')
        for item in items:
            result = {}
            a = item.find('a')
            title = a.get_text()
            title = title[:title.rfind('_')]
            result[title] = [a.get('href')]
            result[title].append(item.find(class_='abstract').get_text())
            search_results.append(result)
        return search_results

    

