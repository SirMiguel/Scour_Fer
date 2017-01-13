from bs4 import BeautifulSoup

from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

class Webpage:
    def __init__(self, url, keywords):
        if (keywords is None):
            self.url = url
            self.body = ""
            self.keywords = []
            self.links = []
        else:
            self.url = url
            self.body = ""
            self.keywords = keywords
            self.links = []



    def harvestKeywords(self):
        self.keywords.extend(self.getMetaTags())
        self.keywords.extend(self.getTitle())


    def getTitle(self):
        self.htmlSouper()
        titles = []
        soup = BeautifulSoup(self.body, 'html.parser')
        for tag in soup.find_all('title'):
            keyword = tag.get("")
            titles.append(keyword)
        return titles





