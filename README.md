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
# open a psql client from postgis instance
$ docker-compose exec postgis psql -U postgres -W postgres

# import Postal Codes data
postgres@[local] ~>COPY postal_codes(the_geom, code, id) from '/var/data/postal_codes.csv' delimiter ',' CSV HEADER;
# import Paystats data
postgres@[local] ~>COPY paystats(amount, p_month, p_age, p_gender, postal_code_id, id) from '/var/data/paystats.csv' delimiter ',' CSV HEADER;

```

#### Fetch data from API
API endpoints are protected by a Token http header, use `Authorization Token secret-key-1` to access.
Import `geo.gs.postman_collection.json` into postman to use prebuilt calls

