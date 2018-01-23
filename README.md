# GEOGRAPHICA TEST


## Setup
#### Docker instances
Run following commands to build & run machines
```bash
$ docker-compose build
$ docker-compose up
```

#### Run migrations on main web instance
```bash
$ docker-compose exec web python manage.py db upgrade
```

#### Import data from CSV's
Copy files into `ext-data` directory, postgis instance mounts this path on its `/var/data`

```bash
# open a psql client from postgis instance, use `postgres` when asked for password
$ docker-compose exec postgis psql -U postgres -W postgres

# import Postal Codes data
postgres@[local] ~>COPY postal_codes(the_geom, code, id) from '/var/data/postal_codes.csv' delimiter ',' CSV HEADER;
# import Paystats data
postgres@[local] ~>COPY paystats(amount, p_month, p_age, p_gender, postal_code_id, id) from '/var/data/paystats.csv' delimiter ',' CSV HEADER;

```

#### Fetch data from API
API endpoints are protected by a Token http header, use `Authorization Token secret-key-1` to access.
Import `geo.gs.postman_collection.json` into postman to use prebuilt calls

Valid enpoints are:
- /paystats
  - To get all data for postal codes with geo info
- /total
  - To get all aggregated amount
- /age-gender
  - To get amount by age & gender
- /age-gender-ts
  - To get amount by timeseries and gender


#### DUMP your data
As CSV flat file
```bash
# open a psql client from postgis instance, use `postgres` when asked for password
$ docker-compose exec postgis psql -U postgres -W postgres
# export paystats table as a CSV flat file
postgres@[local] ~>COPY paystats TO '/var/data/paystats.csv' CSV HEADER;

```

As a full PSQL backup, including schema and indices
```bash
# open a shell session
$ docker-compose exec postgis bash
# execute PSQL pg_dump client utility
/usr/local# pg_dump -U postgres -W postgres > /var/data/all_data.sql
```
