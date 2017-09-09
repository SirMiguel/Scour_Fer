from .Webpage import Webpage
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import logging

class WebCrawler:
    def __init__(self, seed):
        self.toCrawl = self.addWebpages(seed)
        self.crawled = []
        self.nextDepth = []
        self.currentDepth = 0


    def addWebpages(self, urls):
        webpages = []
        for url in urls:
            webpages.append(Webpage(url, None))
        return webpages


    # gets the current webpage
    def openURL(self, url):
        try:
            return urllib.request.urlopen(url)
        except urllib.error.URLError:
            raise

    # Gets the body of the webpage (from the given url)
    def getBody(self, url):
         return bytes.decode(self.openURL(url).read())

    # validates whether a supplied link is a valid url
    def isValidLink(self, url):
        if url is not None:
            try:
                self.openURL(url)
                return True
            except (urllib.error.URLError, ValueError):
                logging.debug("Can't find website " + url)
        return False

    """To be joined refers the array where elements are appended to from to the toJoin array"""
    def union(self, toBeJoined, toJoin):
        for element in toJoin:
            if element not in toBeJoined:
                toBeJoined.extend(toJoin)


    def crawlLinks(self, webpage):
        # For the webpage supplied a list of links with the type of Webpage is returned, containing the URL and associated keywords linking it to this the supplied webpage
        # NOTE: Note all links gathered are validated at this point to ensure only legit links are added (rather slow, but I think worth it)
        links = []
        soup = BeautifulSoup(webpage.body, 'html.parser')
        for link in soup.find_all('a'):
            url = link.get('href')
            #validate link
            if self.isValidLink(url):
                #Keywords takes values in the anchor tag that are likely to contain relevant keywords
                keywords = [link.get("contents"), link.get("alt"), link.get("title"), link.get("string"),link.get("text")]
                links.append(Webpage(url, list(filter(None, keywords))))
        return links

    #gets the title of a webpage from the tag
    def getInTag(self, body, startTag, endTag):
        return body[body.find(startTag) + len(startTag): body.find(endTag)]

    def crawlWeb(self, maxDepth):
        while self.toCrawl and self.currentDepth <= maxDepth:
            currentPage = self.toCrawl.pop()# popping the seed from the list

            if currentPage not in self.crawled:
                currentPage.body = self.getBody(currentPage.url)

                try:
                    currentPage.keywords.append(self.getInTag(currentPage.body, "<title>", "</title>"))
                except TypeError:
                    logging.log(0, 'No title found in ', currentPage.url)

                currentPage.links = self.crawlLinks(currentPage) #Creates a list of webpage objects

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