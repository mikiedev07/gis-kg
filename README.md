# gis-kg

### Setup

The first thing to do is to clone the repository

```shell
$ git clone https://github.com/mikiedev07/gis-kg.git
$ cd gis-kg
```

Run the project via Docker (docker compose). Go to directory gis_kg_dj with Dockerfile and docker-compose.yml files.

```shell
docker compose up -d
```

Type in your browser 127.0.0.1:1111 and you should see Swagger documentation.

### API

The API to application is described below

#### Get the list of Regions

```shell
curl -X 'GET' \
  'http://127.0.0.1:1111/regions/' \
  -H 'accept: application/json'
```

#### Get Region object by id:

```shell
curl -X 'GET' \
  'http://127.0.0.1:1111/regions/{id}/' \
  -H 'accept: application/json'
```

Response schema:
```shell
{
  "id": 0,
  "districts": [
    {
      "id": 0,
      "cantons": [
        {
          "id": 0,
          "title": "string",
          "geometry": "string",
          "district": 0
        }
      ],
      "title": "string",
      "geometry": "string",
      "region": 0
    }
  ],
  "title": "string",
  "geometry": "string"
}
```

As you can see, the customer receives not only the object of the region but also the 
objects of the districts and cantons included in it.

In the same way, when obtaining a district object by its ID, the client will also receive all the cantons included within it.

### Export PostgreSQL data

The data from three tables Region, District, and Canton have been exported to psql_json_data folder in JSON file format using the command

```shell
COPY (
  SELECT json_agg(row_to_json(<table_name>)) :: text
  FROM table_name
) to '<path>';
```

As a result, three files were obtained:
* region.json
* districts.json
* cantons.json

Additionally, in the psql_json_data directory, there is a script pdata_script.json provided for creating the database. 
This file was obtained using the pg_dumpall utility.

The geometric data is represented in the WKT (Well-Known Text) format with SRID (Spatial Reference ID) 4326.





