#!usr/bin/python3
# sequence class

class Sequence(object):

    def __init__(self, accession, accession_link, collection_date, country):
        self.accession = accession
        self.accession_link = accession_link
        self.collection_date = collection_date
        self.country = country