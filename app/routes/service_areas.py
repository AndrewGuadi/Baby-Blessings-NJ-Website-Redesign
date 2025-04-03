import os
import json
from flask import Blueprint, render_template, current_app

service_areas = Blueprint('service_areas', __name__, url_prefix='/service-areas')

def load_area_data(filename):
    data_path = os.path.join(current_app.root_path, 'data', 'service_areas', filename)
    with open(data_path) as f:
        return json.load(f)

@service_areas.route('/')
def index():
    return render_template('service_areas/service_areas.html')

@service_areas.route('/northern-new-jersey')
def northern_new_jersey():
    area_data = load_area_data('northern_new_jersey.json')
    return render_template('service_areas/location_template.html', area_data=area_data)

@service_areas.route('/new-york-city')
def new_york_city():
    area_data = load_area_data('new_york_city.json')
    return render_template('service_areas/location_template.html', area_data=area_data)

@service_areas.route('/westchester')
def westchester():
    area_data = load_area_data('westchester.json')
    return render_template('service_areas/location_template.html', area_data=area_data)

@service_areas.route('/philadelphia')
def philadelphia():
    area_data = load_area_data('philadelphia.json')
    return render_template('service_areas/location_template.html', area_data=area_data)

@service_areas.route('/central-new-jersey')
def central_new_jersey():
    area_data = load_area_data('central_new_jersey.json')
    return render_template('service_areas/location_template.html', area_data=area_data)

@service_areas.route('/long-island')
def long_island():
    area_data = load_area_data('long_island.json')
    return render_template('service_areas/location_template.html', area_data=area_data)
