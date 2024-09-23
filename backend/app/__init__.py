from flask import Flask
from flask_cors import CORS
from .routes import task_routes

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(task_routes, url_prefix='/')

    return app
