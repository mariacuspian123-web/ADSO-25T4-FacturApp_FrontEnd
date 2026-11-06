from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importación de todos los controladores
    from src.controllers.home_controllers import home_bp
    from src.controllers.clients_controllers import clients_bp
    from src.controllers.products_controllers import products_bp
    from src.controllers.users_controller import users_bp
    from src.controllers.categories_controller import categories_bp

    # Registro de Blueprints en la aplicación
    app.register_blueprint(home_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(categories_bp)

    return app


