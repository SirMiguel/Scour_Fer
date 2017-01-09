import urllib.request
from bs4 import BeautifulSoup
import logging

from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

class Webpage:
    url = ""
    body = ""
    keywords = []
    links = []

    def __init__(self, url):
        self.url = url

    #gets the current webpage
    def openURL(self, url):
        try:
            return urllib.request.urlopen(url)
        except:
            raise ValueError(urllib.Error.URLError)

    #Gets the body of the webpage (from the given url)
    def getBody(self):
        self.body = bytes.decode(self.openURL(self.url).read())

    #validates whether a supplied link is a valid url
    def isValidLink(self, url):
        if url is not None:
            try:
                self.openURL(url)
                return True
            except:
                logging.debug("Can't find website " + url)
                print("Can't find website " + url)
                pass
        return False

    def getAllLinks(self):
        # gets all the links of the current webpage
        # NOTE: As of yet not all links gathered are legit links, as it only gathers the href: part of any anchor tag
        soup = BeautifulSoup(self.body, 'html.parser')
        for link in soup.find_all('a'):
            url = link.get('href')
            # validate link
            if self.isValidLink(url):
                print(link.get('title'))
                self.links.append(url)
        return self.links

    def getMetaTags(self):
        soup = BeautifulSoup(self.body, 'html.parser')
        for tag in soup.find_all('meta'):
            keyword = tag.get('content')
            print(keyword)
            self.keywords.append(keyword)

