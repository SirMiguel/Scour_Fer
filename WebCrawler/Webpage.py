import urllib.request
from bs4 import BeautifulSoup
import logging


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
        return bytes.decode(self.openURL(self.url).read())

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

    #gets all the links of the current webpage
    def getAllLinks(self):
        # Gets all the links from a supplied page
        # NOTE: As of yet not all links gathered are legit links, as it only gathers the href: part of any anchor tag
        soup = BeautifulSoup(self.body, 'html.parser')
        for link in soup.find_all('a'):
            url = link.get('href')
            # validate link\
            if self.isValidLink(url):
                print(link.get('title'))
                self.links.append(url)

   # def getMetaTags(self):

