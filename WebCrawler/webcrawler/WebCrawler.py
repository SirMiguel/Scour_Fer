from .Webpage import Webpage
from bs4 import BeautifulSoup
import urllib.request
import logging

class WebCrawler:
    def __init__(self, seed):
        self.toCrawl = seed
        self.crawled = []
        self.nextDepth = []
        self.currentDepth = 0

    def addWebpages(self, urls):
        webpages = []
        for url in urls:
            webpages.append(Webpage(url))
        return webpages

    # gets the current webpage
    def openURL(self, url):
        try:
            return urllib.request.urlopen(url)
        except:
            raise ValueError(urllib.Error.URLError)

    # Gets the body of the webpage (from the given url)
    def getBody(self, url):
         return bytes.decode(self.openURL(url).read())

    # validates whether a supplied link is a valid url
    def isValidLink(self, url):
        if url is not None:
            try:
                self.openURL(url)
                return True
            except:
                logging.debug("Can't find website " + url)
                #print("Can't find website " + url)
                pass
        return False

    """To be joined refers the array where elements are appended to from to the toJoin array"""
    def union(self, toBeJoined, toJoin):
        for element in toJoin:
            if element not in toBeJoined:
                toBeJoined.extend(toJoin)

    def getAllLinks(self, pageBody):
        # gets all the links of the current webpage
        # NOTE: As of yet not all links gathered are legit links, as it only gathers the href: part of any anchor tag
        links = []
        soup = BeautifulSoup(pageBody, 'html.parser')
        for link in soup.find_all('a'):
            url = link.get('href')
            # validate link
            if self.isValidLink(url):
                #print(link.get('title'))
                links.append(url)
        return links

    def crawlWeb(self, maxDepth):
        while self.toCrawl and self.currentDepth <= maxDepth:
            currentPage = Webpage(self.toCrawl.pop())  # popping the seed from the list

            if currentPage.url not in self.crawled:
                currentPage.body = self.getBody(currentPage.url)
                currentPage.links = self.getAllLinks(currentPage.body)
                currentPage.keywords = currentPage.getMetaTags()
                print(currentPage.url)
                print(currentPage.keywords)
                print("\n\n\n\n")
                self.union(self.nextDepth, currentPage.links)
                self.crawled.append(currentPage.url)

            if not self.toCrawl:
                self.toCrawl.extend(self.nextDepth)
                self.nextDepth = []
                self.currentDepth += 1

        return self.crawled