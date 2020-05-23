#!usr/bin/python3
# insert a list of Sequence objects into the PostgreSQL database

import reprlib
import psycopg2
from config import config
from sequence import Sequence

def insert_sequences(seq_list):
	""" insert sequence into accession table """
	insert_query = """INSERT INTO accession(accession, accession_link, collection_date, country)
			VALUES"""

	# connect to server
	conn = None
	access_id = None

	try:
		# get values from the Sequence list
		data = ()

		for seq in seq_list:
			data = data + (seq.accession, seq.accession_link, seq.collection_date, seq.country)
			insert_query += "(%s, %s, %s, %s), "

		insert_query = insert_query[:-2]
		insert_query += " ON CONFLICT (accession) DO NOTHING;"

		# print(data)
		params = config()
		conn = psycopg2.connect(**params)
		cursor = conn.cursor()
		cursor.execute(insert_query, data)
		conn.commit()
		cursor.close()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()