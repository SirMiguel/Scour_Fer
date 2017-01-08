import urllib.request
from bs4 import BeautifulSoup


class Webpage:
    url = ""
    body = ""
    keywords = []
    links = []

    def __init__(self, url):
        self.url = url

    def getPage(self):
        try:
            return urllib.request.urlopen(self.url)
        except:
            raise ValueError(urllib.Error.URLError)

    def getBody(self):
        return bytes.decode(self.getPage(self.url).read())

    def getMetaTags(self):

