from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'UEUEHUEHEUHEUH'

    from .app import index
    from .app import pecas
    
    app.register_blueprint(blueprint=index, url_prefix='/')
    app.register_blueprint(blueprint=pecas, url_prefix='/pecas')

    
    return app

