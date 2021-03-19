# this module build the index by defining the schema and by adding all the documents

import os, os.path
from whoosh import index
from whoosh.index import create_in
from whoosh.fields import *
import pdfplumber as reader


class IndexBuilder:
    index_dir = "./unise/resources/index"           # the directory where the index is stored

    data_dir = "./unise/resources/data"
    test_data_dir = "./unise/resources/test_data"

    schema = Schema(
        title=TEXT(stored=True),        # file and document name
        path=ID(stored=True),           # the file path
        content=TEXT,                   # the document's content
        subject=TEXT(sortable=True),    # the subject of the document (analisi1, algebra, ...)
        year=NUMERIC(sortable=True),    # the year of the course (1° anno, 2° anno, ...)
        course=TEXT(sortable=True),     # from which course the documents come from (scienze_informatiche, biologia,...)
    )

    def create(self, test=False):
        if not os.path.exists(self.index_dir):
            os.mkdir(self.index_dir)

        ix = index.create_in(self.index_dir, self.schema)       # this command clear the index if it exists

        writer = ix.writer(limitmb=512)

        if test:
            path = self.test_data_dir
        else:
            path = self.data_dir

        for course in os.listdir(path):
            for year in os.listdir(path+"/"+course):
                for subject in os.listdir(path+"/"+course+"/"+year):
                    for file in os.listdir(path+"/"+course+"/"+year+"/"+subject):
                        with reader.open(path+"/"+course+"/"+year+"/"+subject+"/"+file) as pdf:
                            content = " ".join([page.extract_text() if page.extract_text() is not None else " " for page in pdf.pages])
                            writer.add_document(
                                title = file,
                                path = path+"/"+course+"/"+year+"/"+subject+"/"+file,
                                content = content,
                                subject = subject.replace("_", " "),
                                year = year,
                                course = course
                            )
        writer.commit()