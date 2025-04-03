from flask import Blueprint, render_template

services = Blueprint('services', __name__, url_prefix='/services')

@services.route('/')
def services_index():
    return render_template('services/services.html')


@services.route('/baby-blessings')
def baby_blessings():
    return render_template('baby-blessings.html')

@services.route('/baptisms')
def baptisms():
    return render_template('services/baptisms.html')

@services.route('/celebrations')
def celebrations():
    return render_template('services/celebrations.html')

@services.route('/naming-ceremonies')
def naming_ceremonies():
    return render_template('services/naming-ceremonies.html')

@services.route('/gallery')
def gallery():
    return render_template('services/gallery.html')
