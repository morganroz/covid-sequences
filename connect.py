#!/usr/bin/python
import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # get config info from file
        params = config()

        # make a connection with the config file
        print('Connecting to the database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # get and print the db version
        print('PostgreSQL version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
       
	    # close cursor
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # make sure the connection is closed before exiting
        if conn is not None:
            conn.close()
            print('Database connection closed.')

# to run this code on its own
if __name__ == '__main__':
    connect()