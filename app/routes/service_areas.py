import json
from flask import Blueprint, render_template

service_areas = Blueprint('service_areas', __name__, url_prefix='/service-areas')

@service_areas.route('/')
def index():
    return render_template('service_areas/service_areas.html')

@service_areas.route('/northern-new-jersey')
def northern_new_jersey():
    with open('service_areas/data/northern_new_jersey.json') as f:
        area_data = json.load(f)
    return render_template('service_areas/location_template.html', area_data=area_data)

@service_areas.route('/new-york-city')
def new_york_city():
    with open('service_areas/data/new_york_city.json') as f:
        area_data = json.load(f)
    return render_template('service_areas/location_template.html', area_data=area_data)

@service_areas.route('/westchester')
def westchester():
    with open('service_areas/data/westchester.json') as f:
        area_data = json.load(f)
    return render_template('service_areas/location_template.html', area_data=area_data)

@service_areas.route('/philadelphia')
def philadelphia():
    with open('service_areas/data/philadelphia.json') as f:
        area_data = json.load(f)
    return render_template('service_areas/location_template.html', area_data=area_data)

@service_areas.route('/central-new-jersey')
def central_new_jersey():
    with open('service_areas/data/central_new_jersey.json') as f:
        area_data = json.load(f)
    return render_template('service_areas/location_template.html', area_data=area_data)

@service_areas.route('/long-island')
def long_island():
    with open('service_areas/data/long_island.json') as f:
        area_data = json.load(f)
    return render_template('service_areas/location_template.html', area_data=area_data)
