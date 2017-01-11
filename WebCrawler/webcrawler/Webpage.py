from bs4 import BeautifulSoup

from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

class Webpage:
    def __init__(self, url):
        self.url = url
        body = ""
        keywords = []
        links = []

    def getKeywords(self):
        self.keywords.extend(self.getMetaTags())

    def getMetaTags(self):
        soup = BeautifulSoup(self.body, 'html.parser')
        for tag in soup.find_all('meta'):
            keyword = tag.get('content')
            print(keyword)
            self.keywords.append(keyword)

