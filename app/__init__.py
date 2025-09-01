from flask import *
from .hello.routes import hello_bp, hello_name

def create_app():
    app = Flask(__name__)

    app.register_blueprint(hello_bp)
    app.register_blueprint(hello_name)

    return app