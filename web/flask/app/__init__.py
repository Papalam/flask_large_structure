from flask import Flask

from config import Config
from app.extensions import mysql


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    mysql.init_app(app)

    # Register blueprints here
    from app.main import main as main_section
    app.register_blueprint(main_section)

    from app.fedex import fedex
    app.register_blueprint(fedex, url_prefix='/fedex')

    @app.route('/test')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
