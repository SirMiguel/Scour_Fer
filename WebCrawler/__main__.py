from WebCrawler.webcrawler import Webpage



def main():
    seed = ["https://jeffknupp.com/blog/2014/09/01/what-is-a-nosql-database-learn-by-writing-one-in-python/"]  # either to be a list or just one website
    links = crawlWeb(seed, 2)
    print(links)
    print(links.__len__())


if  __name__ =='__main__':
    main()