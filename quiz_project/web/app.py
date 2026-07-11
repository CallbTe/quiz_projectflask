from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "superdupersecretkey"

    from web.routes import register_routes
    register_routes(app)

    return app