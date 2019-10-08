import json, os

from flask import Flask, request
import psycopg2
from psycopg2.extras import RealDictCursor

try:
    conn = psycopg2.connect("dbname='pyindia' user='py' host='gis.georeactor.com' password='zim'") # port=####
except:
    print("I am unable to connect to the database")

cursor = conn.cursor(cursor_factory=RealDictCursor)

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/about')
def about():
    """
    return a simple list of stats about this point:
    - which state and district is it in?
    -- download the district GeoJSON
    - how far is it from health facilities?
    """
    cursor.execute("""
            SELECT
                st_name,
                pc_name,
                ST_AsGeoJSON(wkb_geometry) AS geojson
            FROM parliament
            WHERE ST_Intersects(
                wkb_geometry,
                ST_MakePoint(%s, %s)
            )""",
        (request.args.get('lng'), request.args.get('lat')))
    result = cursor.fetchone()

    if result is None:
        return json.dumps({"st_name": "Foreign", "pc_name": "Foreign"})
    else:
        cursor.execute("""
                SELECT
                    zone_name,
                    ward_no,
                    ST_AsGeoJSON(wkb_geometry) AS geojson
                FROM chennai_wards
                WHERE ST_Intersects(
                    wkb_geometry,
                    ST_MakePoint(%s, %s)
                )""",
            (request.args.get('lng'), request.args.get('lat')))
        ward = cursor.fetchone()
        if ward is not None:
            result["ward"] = ward["geojson"]

        return json.dumps(result)

@app.route('/messy')
def messy():
    """
    attempt to drop the trains table
    """
    cursor.execute("DROP TABLE trains")
    result = cursor.fetchone()
    return json.dumps(result)

@app.route('/messy2')
def messy2():
    """
    attempt to modify the trains table
    """
    cursor.execute("INSERT INTO trains (start, finish) VALUES ('Atlantic Ocean', 'Indian Ocean')")
    result = cursor.fetchone()
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)
