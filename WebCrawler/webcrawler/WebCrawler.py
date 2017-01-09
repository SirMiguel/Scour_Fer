"""from . import Webpage

from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

#To be joined refers the array where elements are appended to from to the toJoin array
def union(toBeJoined, toJoin):
    for element in toJoin:
        if element not in toBeJoined:
            toBeJoined.extend(toJoin)



def crawlWeb(seed, maxDepth):
    toCrawl = []
    for webpage in seed:
        toCrawl.append(Webpage(webpage))

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

seed = "https://jeffknupp.com/blog/2014/09/01/what-is-a-nosql-database-learn-by-writing-one-in-python/"  #either to be a list or just one website
links = crawlWeb(seed, 1)
print(links)
print(links.__len__())



"""