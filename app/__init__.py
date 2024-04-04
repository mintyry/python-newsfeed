from flask import Flask
from app.routes import home, dashboard
from app.db import init_db

def create_app(test_config=None):
# set up app config
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    # decorator; turns hello fn into a route
    @app.route('/hello')
    # make inner function hello()
    def hello():
        # return becomes route's response
        return 'hello world'
    
    # register routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    
    # pass in app to make logic happen in db/__init__.py
    init_db(app)

    return app


# @app.route('/')
# def hello():
#     return 'Hello, World!'

