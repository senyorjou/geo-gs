## GEOGRAPHICA TEST


### Setup
##### Docker instances
Run following commands to build & run machines
```bash
$ docker-compose build
$ docker-compose up
```

##### Run migrations on main web instance
```bash
$ docker-compose exec web python manage.py db upgrade
```

##### Import data from CSV's
```bash
# open a psql client from postgis instance
$ docker-compose exec postgis psql -U postgres -W postgres

# import Postal Codes data
postgres@[local] ~>COPY postal_codes(the_geom, code, id) from '/var/data/postal_codes.csv' delimiter ',' CSV HEADER;
# import Paystats data
postgres@[local] ~>COPY paystats(amount, p_month, p_age, p_gender, postal_code_id, id) from '/var/data/paystats.csv' delimiter ',' CSV HEADER;

```

