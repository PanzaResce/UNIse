from unise.indexbuilder import IndexBuilder
from unise.searcher import searcher


class UNIse:

    @staticmethod
    def run(mode = "batch"):
        print("UNIse running...")
        builder = IndexBuilder()
        #builder.create(test=True)

        mysearcher = searcher()
        res = mysearcher.search("fisica", "content", "subject", "year", sort_term="")


        print(res)