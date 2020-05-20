#!usr/bin/python3
# script to read the yaml data from ncbi into a dictionary

import yaml
from sequence import Sequence
import reprlib # for limiting print output

with open(r'data/ncov-sequences.yaml') as file:
    seq_file = yaml.full_load(file)

    # read the .yaml into a dict
    raw_data = {}
    for item, doc in seq_file.items():
        raw_data[item] = doc

    # loop over each sequence
    seqs = []
    for seq in raw_data['genbank-sequences']:
        new_seq = Sequence(seq['accession'], seq['accession-link'], seq['collection-date'], seq['country'])
        seqs.append(new_seq)

