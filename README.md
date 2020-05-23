# covid-sequences

## config

### postgresql database configuration

#### in postgresql

1. Create a postgres database for the sequence data
2. Create a table called "accession" with the following fields:
{
	- accessid
	- accession
	- accession_link
	- collection_date
	- country
}

```sql
CREATE TABLE accession
(
    access_id integer NOT NULL DEFAULT nextval('accession_access_id_seq'::regclass),
    accession character varying(20) COLLATE pg_catalog."default" NOT NULL,
    accession_link character varying(100) COLLATE pg_catalog."default" NOT NULL,
    collection_date timestamp without time zone,
    country character varying(30) COLLATE pg_catalog."default",
    CONSTRAINT accession_pkey PRIMARY KEY (access_id),
    CONSTRAINT accession_accession_key UNIQUE (accession),
    CONSTRAINT accession_accession_link_key UNIQUE (accession_link)
)
```

#### in python

3. Create a configuration file called "database.ini" with the following format:

```
[postgresql]
host=localhost
database=postgres
user=postgres
password=postgres
```