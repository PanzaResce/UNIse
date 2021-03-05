import whoosh.index as index
import nltk
from whoosh import qparser
from indexbuilder import indexbuilder
from nltk.corpus import wordnet as wn


class searcher:

    def __init__(self):
        self.index_dir = indexbuilder.index_dir
        self.index = index.open_dir(self.index_dir)

        self.english_vocab = set(w.lower() for w in nltk.corpus.words.words())

    def search(self, query, *fields):

        expanded_query = self.expand_query(query)
        q = self.parse_query(expanded_query, *fields)

        with self.index.searcher() as s:
            results = s.search(q)
            if len(results) == 0:
                q = self.parse_query(expanded_query, *fields, group="OR")
                results = s.search(q)

            print(q)
            print(len(results))
            print(results[0:len(results)])

    def parse_query(self, query, *fields, group="AND"):
        if group == "OR":
            parser = qparser.MultifieldParser(fields, schema=self.index.schema, group=qparser.OrGroup)
        else:
            parser = qparser.MultifieldParser(fields, schema=self.index.schema)

        q = parser.parse(query)

        return q

    def expand_query(self, query):
        """Translates all the terms in the query from ita to eng and vice versa,
        the translated term has half the relevance in the query"""

        q = ""
        for w in query.split():
            q += w
            q += " "

            w_lang = self.detect_language(w)
            try:
                if w_lang == "en":
                    q += "OR " + wn.synset(wn.synsets(w)[0].name()).lemma.names("ita") + "^0.5 "
                elif w_lang == "ita":
                    q += "OR " + wn.lemmas(w, lang="ita")[0].synset().name().split(".")[0] + "^0.5 "
            except IndexError as e:
                # error raised when no synsets or lemmas are found
                print("error: " + type(e).__name__)

        return q

    def detect_language(self, term):
        """Detect if language is ITA or ENG"""
        if term in self.english_vocab:
            return "en"
        else:
            return "ita"
