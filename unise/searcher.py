import whoosh.index as index
import nltk
from whoosh import qparser
from unise.indexbuilder import IndexBuilder
from nltk.corpus import wordnet as wn


class searcher:

    def __init__(self):
        self.index_dir = IndexBuilder.index_dir
        self.index = index.open_dir(self.index_dir)

        self.english_vocab = set(w.lower() for w in nltk.corpus.words.words())

    def search(self, query, *fields, sort_term, hit_count=10):

        print(query)

        results = list()

        expanded_query = self.expand_query(query)
        q = self.parse_query(expanded_query, *fields)

        print(q)

        with self.index.searcher() as s:
            out = s.search(q, limit=hit_count, sortedby=sort_term)
            if len(out) == 0:
                q = self.parse_query(expanded_query, *fields, group="OR")
                out = s.search(q, limit=hit_count, sortedby=sort_term)

            self.copy(results, out, hit_count)

        return results

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
            except (IndexError, AttributeError) as e:
                # Index error raised when no synsets or lemmas are found
                # AttributeError usually raised when there is no translation between languages
                print("error: " + type(e).__name__)

        return q

    def detect_language(self, term):
        """Detect if language is ITA or ENG"""
        if term in self.english_vocab:
            return "en"
        else:
            return "ita"

    @staticmethod
    def copy(results, struct, hit_count):
        """ Self defined deep copy """
        out_len = hit_count if len(struct) > hit_count else len(struct)
        for i in range(out_len):
            app = dict()
            for key in struct[i]:
                x = key
                y = struct[i][key]
                app[x] = y

            results.append(app)