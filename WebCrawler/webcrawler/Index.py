from WebCrawler.webcrawler import Record


class Index:
    def __init__(self, records):
        self.records = records

    def in_index(self, keyword):
        for element in self.records:
            if element[0] == keyword:
                return True
        return False

    def get_index(self, keyword):
        for element in self.records:
            if element[0] == keyword:
                return self.records.index(element)

    def add_to_index(self, keyword, url):
        if not self.in_index(keyword):
           # element = [keyword, [url]]
           # self.records.append(element)

           element = Record(keyword, url)
           self.records.append(element)
        else:
            self.records[self.get_index(keyword)]
            self.records[self.get_index(keyword)][1].append(url)
            self.records[self.get_index(keyword)]

