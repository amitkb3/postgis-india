# Step 2

Where do I find geo data for my website?

To make the tutorial as relevant as possible, I want to show how it's possible to
download information about my workshop country (in this case, India) and import
it into PostGIS.  This can be difficult to install and troubleshoot, so I might end
up showing most of this on the projector. Even if students cannot import data in the workshop, they can run future steps with the tables in the PostGIS cloud instance or the Jupyter notebooks.

All of these datasets will be imported into a PostGIS database (PostgreSQL + extensions).

Data will be used in the later steps.

### Installing and running locally

Install ogr2ogr by installing GDAL.

### Interactive Tutorial

Here we are talking about different data sources. I'm interested to hear where
PyCon attendees have found good geo-data before.

- Downloading parliament and assembly districts, cities, states, census districts

https://github.com/datameet/maps
https://github.com/datameet/Municipal_Spatial_Data

- Other public data, including farming / agricultural data

https://data.gov.in/

- Downloading OSM data

(TBD: brief intro to OpenStreetMap)

There are tons of community-built data on OpenStreetMap (OSM) including roads and buildings

I used http://overpass-turbo.eu/ to search for wells, restaurants, hotels, etc.

```
node
  [man_made=water_well]
  ({{bbox}});
out;
```

You can also download places with a Tamil name

```
node
  [name:ta]
  ({{bbox}});
out;
```

- Importing Geo CSVs

There's a good example in Step 4 of uploading a CSV which has latitude and longitude.

### Learnings

- Do attendees know good sources for local open data?
- What is OpenStreetMap?
- How can I get data to make quality websites?
- Links for installing ogr2ogr on my computer
