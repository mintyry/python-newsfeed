from flask import Flask

def create_app(test_config=None):
# set up app config
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    # decorator; turns hell fn into a route
    @app.route('/hello')
    # make inner function hello()
    def hello():
        # return becomes route's response
        return 'hello world'
    
    return app


# @app.route('/')
# def hello():
#     return 'Hello, World!'

