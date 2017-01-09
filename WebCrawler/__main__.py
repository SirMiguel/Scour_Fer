from WebCrawler.webcrawler import Webpage

"""To be joined refers the array where elements are appended to from to the toJoin array"""
def union(toBeJoined, toJoin):
    for element in toJoin:
        if element not in toBeJoined:
            toBeJoined.extend(toJoin)

def add_webpages(urls):
    webpages = []
    for url in urls:
        webpages.append(Webpage.Webpage(url))
    return webpages



def crawlWeb(seed, maxDepth):
    toCrawl = add_webpages(seed)
    crawled = [] #where I wanna load up the current index and get websites already indexed
    nextDepth = []
    currentDepth = 0
    while toCrawl and currentDepth <= maxDepth:
        page = toCrawl.pop() #poping the seed from the list

        if page.url not in crawled:
            try: page.getBody()
            except: pass
            page.getAllLinks()
            union(nextDepth, add_webpages(page.links))

            crawled.append(page.url)

        if not toCrawl:
            toCrawl.extend(nextDepth)
            nextDepth = []
            currentDepth += 1

    return crawled





def main():
    seed = ["https://jeffknupp.com/blog/2014/09/01/what-is-a-nosql-database-learn-by-writing-one-in-python/"]  # either to be a list or just one website
    links = crawlWeb(seed, 2)
    print(links)
    print(links.__len__())


if  __name__ =='__main__':
    main()