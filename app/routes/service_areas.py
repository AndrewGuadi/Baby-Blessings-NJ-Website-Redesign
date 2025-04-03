from flask import Blueprint, render_template

service_areas = Blueprint('service_areas', __name__, url_prefix='/service-areas')


@service_areas.route('/service_areas')
def service_areas():
    return render_template('service_areas.html')

@service_areas.route('/northern-new-jersey')
def northern_new_jersey():
    return render_template('service_areas/northern-new-jersey.html')

@service_areas.route('/new-york-city')
def new_york_city():
    return render_template('service_areas/new-york-city.html')

@service_areas.route('/westchester')
def westchester():
    return render_template('service_areas/westchester.html')

@service_areas.route('/philadelphia')
def philadelphia():
    return render_template('service_areas/philadelphia.html')

@service_areas.route('/central-new-jersey')
def central_new_jersey():
    return render_template('service_areas/central-new-jersey.html')

@service_areas.route('/long-island')
def long_island():
    return render_template('service_areas/long-island.html')
