class Record:
    keyword = ""
    websites_ref = []

    def __init__(self, keyword, websites_ref):
        self.keyword = keyword
        self.websites_ref = websites_ref

    def add_ref_website(self, url):

        self.websites_ref

    def sort_references(self):
        heap = self.websites_ref
        for element in self.websites_ref:
            element = heap.pop(max(heap))
