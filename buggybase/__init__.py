from flask import Flask
from flask_bootstrap import Bootstrap

__version__ = '1.0.0'


def create_app():
    # create and configure the app
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    # apply the blueprints to the app
    from buggybase import base
    app.register_blueprint(base.bp)

    return app
