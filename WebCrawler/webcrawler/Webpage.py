from bs4 import BeautifulSoup

from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

class Webpage:
    def __init__(self, url):
        self.url = url
        self.body = ""
        self.keywords = []
        self.links = []

    def getKeywords(self):
        self.keywords.extend(self.getMetaTags())
        self.keywords.extend(self.getTitle())


    def getTitle(self):
        titles = []
        soup = BeautifulSoup(self.body, 'html.parser')
        for tag in soup.find_all('title'):
            keyword = tag.get("")
            titles.append(keyword)
        return titles


    def getMetaTags(self):
        metatags =[]
        soup = BeautifulSoup(self.body, 'html.parser')
        for tag in soup.find_all('meta'):
            keyword = tag.get('content')
            metatags.append(keyword)
        return metatags
