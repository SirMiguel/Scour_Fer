import urllib.request
from urllib.error import HTTPError
import json
import urllib.robotparser
import re

def getPage(url):
    pageBodyBytes = urllib.request.urlopen(url).read()
    return bytes.decode(pageBodyBytes)

def can_page_be_read(url):
    roboto = urllib.robotparser.RobotFileParser(url)
    roboto.read()
    return roboto.can_fetch("*", url)

def get_all_links(page):
    return set(re.findall(r'http://[a-zA-Z0-9\.]*\.[a-z]{2,}', page)) # find all urls in the content

def crawl_web(seed, depth_interations):
    toCrawl = seed
    crawled = [] #where I wanna load up the current index and get websites already indexed
    nextDepth = []
    while len(toCrawl) > 0 and depth_interations >= 0:
        page = toCrawl.pop() #poping the seed from the list
        if not crawled.__contains__(page):
            print("page", page)
            try:
                pageBody = getPage(page)
                if can_page_be_read(page):
                    all_links_from_page = get_all_links(pageBody)
                    print("Links from", page, ":", all_links_from_page)
                    nextDepth.extend(all_links_from_page)
                crawled.append(page)
            except HTTPError:
                pass

        if not toCrawl:
            toCrawl = nextDepth.copy()
            nextDepth.clear()
            depth_interations -= 1
    return crawled

def read_index():
    return json.load(open('index.json'))

def save_index(index):
    json.dump(index)

#index = read_index()

seed = ["http://www.boddie.org.uk/python/HTML.html"] #either to be a list or just one website
print(crawl_web(seed, 5))