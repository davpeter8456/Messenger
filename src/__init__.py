from flask import Flask




def create_app():
    app = Flask(__name__)

    from src.routes.web_routes import web_bp

    app.register_blueprint(web_bp)

    return app
