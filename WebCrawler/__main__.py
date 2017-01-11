from WebCrawler.webcrawler.WebCrawler import WebCrawler

def main():
    seed = ["https://jeffknupp.com/blog/2014/09/01/what-is-a-nosql-database-learn-by-writing-one-in-python/"]  # either to be a list or just one website
    crawler = WebCrawler(seed)
    links = crawler.crawlWeb(2)
    print(links)
    print(links.__len__())


if  __name__ =='__main__':
    main()