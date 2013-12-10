#-*-coding:utf-8-*- 
import re
import urllib2
from bs4 import BeautifulSoup

def page(title, encoding='utf-8'):
    title = title.replace(' ', '%20')
    PAGE_URL = 'http://baike.baidu.com/search/word?pic=1&enc=%s&word=%s'%(encoding, title)
    return BaikePage(PAGE_URL)

def search(title, results=10, page_n=1):
    pn = (page_n - 1) * results
    SEARCH_URL = 'http://baike.baidu.com/search?pn=%d&rn=%d&word='%(pn, results)
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
        inurls = []
        href = self.soup.find_all(href=re.compile('\/(sub)?view(\/[0-9]*)+.htm'))
        for url in href:
            inurls.append(url.get_text())
        return inurls

    def get_images(self):
        pass

    def get_tags(self):
        tags = []
        for tag in self.soup.find_all(class_=['nslog:7336', 'taglist']):
            tags.append(tag.get_text())
        return tags
    
    def get_references(self):
        references = {}
        for ref in self.soup.find_all(class_='nslog:1968'):
            references[ref.get_text()] = ref.get('href')
        return references

class BaikeSearch(object):
    def __init__(self, url):
        self.http = urllib2.urlopen(url)
        self.html = self.http.read()
        self.soup = BeautifulSoup(self.html)


