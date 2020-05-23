#!usr/bin/python3
# script to read the yaml data from ncbi into a dictionary

import yaml
from sequence import Sequence
import reprlib # for limiting print output

# from connect import connect # for postgresql connection
from insert_sequences import insert_sequences

def validate_date(date):
    try: 
        date_elems = date.split("-")
        if len(date_elems) < 1 or len(date_elems[0]) < 4:
            date_elems[0] = "2000"
        if len(date_elems) < 2:
            date_elems.append("01")
        elif len(date_elems[1]) < 2:
            date_elems[1] = "01"
        if len(date_elems) < 3:
            date_elems.append("01")
        elif len(date_elems[2]) < 2:
            date_elems[2] = "01"
        new_date = "-".join(date_elems)
        return new_date
    except:
        return "2000-01-01"

with open(r'data/ncov-sequences.yaml') as file:
    print("Loading in raw accession file...")
    seq_file = yaml.full_load(file)

    # read the .yaml into a dict
    raw_data = {}
    for item, doc in seq_file.items():
        raw_data[item] = doc
    print("File loaded.")

    # loop over each sequence and put them in a list of Sequence objects
    print("Formatting data...")
    seqs = []
    link = ""
    date = ""
    for seq in raw_data['genbank-sequences']:
        date = validate_date(seq["collection-date"])
        link = seq['accession-link'].split("\"")
        link = link[1]
        new_seq = Sequence(seq['accession'], link, date, seq['country'])
        seqs.append(new_seq)

    print("Uploading to database...")
    insert_sequences(seqs)