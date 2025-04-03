#!/usr/bin/env python3
import os

# Function to create directories if they don't exist
def create_directories(dirs):
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

# Function to create files with given content
def create_file(filepath, content=""):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created file: {filepath}")

def main():
    # Root-level files
    root_files = {
        "run.py": '''#!/usr/bin/env python3
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
''',
        "config.py": '''# Global configuration file
DEBUG = True
SECRET_KEY = "your-secret-key-here"
''',
        "requirements.txt": '''Flask
# Add additional packages here
'''
    }
    
    for filepath, content in root_files.items():
        create_file(filepath, content)
    
    # Create instance directory and config file
    create_directories(["instance"])
    create_file(os.path.join("instance", "config.py"), '''# Instance-specific configuration
# For example, override secret keys or database URIs here.
''')
    
    # Define directories to be created under the app folder
    app_dirs = [
        "app",
        "app/routes",
        "app/templates",
        "app/templates/services",
        "app/templates/service_areas",
        "app/static",
        "app/static/css",
        "app/static/js",
        "app/static/images",
    ]
    create_directories(app_dirs)
    
    # Create app/__init__.py with app factory and blueprint registration
    create_file("app/__init__.py", '''from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    # Register blueprints
    from app.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.routes.services import services as services_blueprint
    app.register_blueprint(services_blueprint)

    from app.routes.service_areas import service_areas as service_areas_blueprint
    app.register_blueprint(service_areas_blueprint)

    from app.routes.testimonials import testimonials as testimonials_blueprint
    app.register_blueprint(testimonials_blueprint)

    return app
''')
    
    # Create a stub models.py
    create_file("app/models.py", "# Database models go here\n")
    
    # Create route files in app/routes
    # __init__.py for routes
    create_file("app/routes/__init__.py", "# This file can be used to import and register all blueprints\n")
    
    create_file("app/routes/main.py", '''from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')
''')
    
    create_file("app/routes/services.py", '''from flask import Blueprint, render_template

services = Blueprint('services', __name__, url_prefix='/services')

@services.route('/baby-blessings')
def baby_blessings():
    return render_template('services/baby-blessings.html')

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
''')
    
    create_file("app/routes/service_areas.py", '''from flask import Blueprint, render_template

service_areas = Blueprint('service_areas', __name__, url_prefix='/service-areas')

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
''')
    
    create_file("app/routes/testimonials.py", '''from flask import Blueprint, render_template

testimonials = Blueprint('testimonials', __name__, url_prefix='/testimonials')

@testimonials.route('/')
def index():
    return render_template('testimonials.html')
''')
    
    # Create templates
    # Base template
    create_file("app/templates/base.html", '''<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Baby Blessings NJ</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <h1>Baby Blessings NJ</h1>
        <!-- Navigation goes here -->
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2025 Baby Blessings NJ</p>
    </footer>
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
''')
    
    # Home template
    create_file("app/templates/home.html", '''{% extends 'base.html' %}
{% block content %}
<h2>Welcome to Baby Blessings NJ</h2>
<p>Your premier officiant service provider for baby blessings, baptisms, and more.</p>
{% endblock %}
''')
    
    # Additional top-level templates
    create_file("app/templates/about-us.html", "<h2>About Us</h2>\n<p>Information about the company.</p>")
    create_file("app/templates/privacy-policy.html", "<h2>Privacy Policy</h2>\n<p>Our privacy practices.</p>")
    create_file("app/templates/contact.html", "<h2>Contact</h2>\n<p>Contact us via this page.</p>")
    create_file("app/templates/testimonials.html", "<h2>Testimonials</h2>\n<p>Our clients’ stories.</p>")
    
    # Create templates for services
    services_templates = {
        "baby-blessings.html": '''{% extends 'base.html' %}
{% block content %}
<h2>Baby Blessings</h2>
<p>Details about our baby blessing ceremonies.</p>
{% endblock %}
''',
        "baptisms.html": '''{% extends 'base.html' %}
{% block content %}
<h2>Baptisms</h2>
<p>Information on baptism services.</p>
{% endblock %}
''',
        "celebrations.html": '''{% extends 'base.html' %}
{% block content %}
<h2>Ceremonial Celebrations</h2>
<p>Details on various celebratory services.</p>
{% endblock %}
''',
        "naming-ceremonies.html": '''{% extends 'base.html' %}
{% block content %}
<h2>Naming Ceremonies</h2>
<p>Details on personalized naming ceremonies.</p>
{% endblock %}
''',
        "gallery.html": '''{% extends 'base.html' %}
{% block content %}
<h2>Gallery</h2>
<p>Our past ceremonies and event highlights.</p>
{% endblock %}
'''
    }
    for filename, content in services_templates.items():
        create_file(os.path.join("app", "templates", "services", filename), content)
    
    # Create templates for service areas
    service_areas_templates = {
        "northern-new-jersey.html": '''{% extends 'base.html' %}
{% block content %}
<h2>Northern New Jersey</h2>
<p>Serving communities in Northern New Jersey.</p>
{% endblock %}
''',
        "new-york-city.html": '''{% extends 'base.html' %}
{% block content %}
<h2>New York City</h2>
<p>Offering services to New York City and nearby areas.</p>
{% endblock %}
''',
        "westchester.html": '''{% extends 'base.html' %}
{% block content %}
<h2>Westchester County</h2>
<p>Providing services in affluent Westchester communities.</p>
{% endblock %}
''',
        "philadelphia.html": '''{% extends 'base.html' %}
{% block content %}
<h2>Philadelphia Metropolitan Area</h2>
<p>Bringing our offerings to the Philadelphia area.</p>
{% endblock %}
''',
        "central-new-jersey.html": '''{% extends 'base.html' %}
{% block content %}
<h2>Central New Jersey</h2>
<p>Serving central New Jersey regions including Princeton and beyond.</p>
{% endblock %}
''',
        "long-island.html": '''{% extends 'base.html' %}
{% block content %}
<h2>Long Island</h2>
<p>Our services extend to Northern Long Island communities.</p>
{% endblock %}
'''
    }
    for filename, content in service_areas_templates.items():
        create_file(os.path.join("app", "templates", "service_areas", filename), content)
    
    # Create basic static asset files
    create_file(os.path.join("app", "static", "css", "style.css"), "/* Add your CSS styles here */")
    create_file(os.path.join("app", "static", "js", "script.js"), "// Add your JavaScript here")

    print("Project structure has been initialized.")

if __name__ == "__main__":
    main()
