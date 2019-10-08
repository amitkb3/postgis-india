# postgis-india

A PostGIS tutorial for PyCon India 2019, with Python as the main language.

How you can help:

- read about PyCon India: https://in.pycon.org/2019/
- donate to the Python Software Foundation: https://www.python.org/psf/

## Participatory

My goal was to create a PostGIS demo which would be accessible to students
if they have not installed libraries ahead of time:

- Basic server config for a read-only PostGIS in the cloud
- Python notebooks connected to PostGIS
- Choice of SQL or ORM to interact with PostGIS

## Topics

- Finding and downloading geodata (govt data, OpenStreetMap)
- Setting up PostGIS
- SQL Review and Added Features in PostGIS
- Importing CSVs and geodata
- Python scripts for import, export, querying
- Sample queries with map frontends: point-in-polygon, nearest point, buffers, statistics, etc

## Setup for public PostGIS and Jupyter Notebooks

I set up on DigitalOcean so that ports and resizing would be more readily available.

The documents linked here are old. The current version of PostgreSQL is '10'

Installing PostgreSQL on Ubuntu:
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04

Installing and configuring PostGIS on Ubuntu:
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postgis-on-ubuntu-14-04

Making PostgreSQL open to the web:
https://bosnadev.com/2015/12/15/allow-remote-connections-postgresql-database-server/

DigitalOcean firewall: https://www.digitalocean.com/community/questions/opening-ports-on-my-server

## License

Open source, MIT license
