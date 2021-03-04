from indexbuilder import indexbuilder
from searcher import searcher

class UNIse:

    @staticmethod
    def run(mode = "batch"):
        print("UNIse running...")
        #builder = indexbuilder()
        #builder.create(test=True)

        mysearcher = searcher()
        mysearcher.search("analisi", "content", "subject")
