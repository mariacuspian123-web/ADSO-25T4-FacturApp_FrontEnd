from flask import Flask

def create_app():
    app = Flask(__name__)

    from src.controllers.home_controller import home_bp
    from src.controllers.clients_controller import clients_bp
    from src.controllers.categories_controller import categories_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(categories_bp)

    return app



