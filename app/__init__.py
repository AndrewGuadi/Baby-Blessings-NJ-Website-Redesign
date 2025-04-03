from flask import Flask

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
