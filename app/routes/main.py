from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/about-us')
def about_us():
    return render_template('about-us.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')