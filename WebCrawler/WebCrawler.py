import urllib.request
import logging
import json
import urllib.robotparser
from bs4 import BeautifulSoup


def getPage(url):
    try:
        return urllib.request.urlopen(url)
    except:
        raise ValueError(urllib.Error.URLError)

def getBody(url):
    return bytes.decode(getPage(url).read())


def union(toBeJoined, toJoin):
    """To be joined refers the array where elements are appended to from to the toJoin array"""
    for element in toJoin:
        if element not in toBeJoined:
            toBeJoined.extend(toJoin)


def getAllLinks(page):
    #Gets all the links from a supplied page
    #NOTE: As of yet not all links gathered are legit links, as it only gathers the href: part of any anchor tag
    links = []
    soup = BeautifulSoup(page, 'html.parser')
    for link in soup.find_all('a'):
        url = link.get('href')
        #validate link\
        if isValidLink(url):
            print(link.get('title'))
            links.append(url)

    return links


def isValidLink(url):
    if url is not None:
        try:
            getPage(url)
            return True
        except:
            logging.debug("Can't find website " + url)
           # print("Can't find website " + url)
            pass
    return False
    # if link[:3] == "www" or link[:4] == "http" or link[:5] == "https":


def crawlWeb(seed, maxDepth):
    toCrawl = [seed]
    crawled = [] #where I wanna load up the current index and get websites already indexed
    nextDepth = []
    currentDepth = 0
    while toCrawl and currentDepth <= maxDepth:
        page = toCrawl.pop() #poping the seed from the list

        if page not in crawled:
            try:
                pageBody = getBody(page)
            except:
                pass

            #nextDepth = getAllLinks(pageBody)
            #nextDepth.extend(getAllLinks(pageBody))
            union(nextDepth, getAllLinks(pageBody)) #Adds all the links of that page to the next depth of pages to crawl
            crawled.append(page)

        if not toCrawl:
            toCrawl.extend(nextDepth)
            nextDepth = []
            currentDepth += 1

    return crawled

def read_index():
    return json.load(open('index.json'))

#def save_index():
#    json.dump(index)

#index = read_index()
#http://www.boddie.org.uk/python/HTML.html

seed = "https://jeffknupp.com/blog/2014/09/01/what-is-a-nosql-database-learn-by-writing-one-in-python/"  #either to be a list or just one website
links = crawlWeb(seed, 1)
print(links)
print(links.__len__())




