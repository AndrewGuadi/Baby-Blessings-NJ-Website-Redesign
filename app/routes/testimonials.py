from flask import Blueprint, render_template

testimonials = Blueprint('testimonials', __name__, url_prefix='/testimonials')

@testimonials.route('/')
def index():
    return render_template('testimonials.html')
