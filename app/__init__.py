# app/__init__.py
from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.context_processor
    def inject_site_links():
        return {
            "GET_STARTED_URL": app.config.get("GET_STARTED_URL"),
            "VOLUNTEER_URL": app.config.get("VOLUNTEER_URL"),
            "INSTAGRAM_URL": app.config.get("INSTAGRAM_URL"),
            "DONATE_URL": app.config.get("DONATE_URL"),

            "FORM_FOOTPRINTS_URL": app.config.get("FORM_FOOTPRINTS_URL"),
            "FORM_COUNSELING_URL": app.config.get("FORM_COUNSELING_URL"),
            "FORM_LIFE_COACHING_URL": app.config.get("FORM_LIFE_COACHING_URL"),
            "FORM_ALT_SENTENCING_URL": app.config.get("FORM_ALT_SENTENCING_URL"),
            "FORM_COMMUNITY_PROGRAMS_URL": app.config.get("FORM_COMMUNITY_PROGRAMS_URL"),
            "FORM_PRO_DEV_URL": app.config.get("FORM_PRO_DEV_URL"),
            "FORM_GET_INVOLVED_URL": app.config.get("FORM_GET_INVOLVED_URL"),
        }


    from app.routes import bp as site_bp
    app.register_blueprint(site_bp)

    return app


