import whoosh.index as index
from whoosh.qparser import MultifieldParser
from indexbuilder import indexbuilder


class searcher:

    def __init__(self):
        self.index_dir = indexbuilder.index_dir
        self.index = index.open_dir(self.index_dir)

    def search(self, query, *fields):
        parser = MultifieldParser(fields, schema=self.index.schema)
        q = parser.parse(query)

        with self.index.searcher() as s:
            results = s.search(q)
            print(len(results))
            print(results[0:len(results)])
