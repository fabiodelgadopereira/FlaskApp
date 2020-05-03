# coding: utf-8
from os import path
from flask import Flask
from .resources.cliente import Customer, Customers
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from .resources.security import authenticate, identity
from flask_jwt import JWT


def create_app(mode):
    instance_path = path.join(
        path.abspath(path.dirname(__file__)), "%s_instance" % mode
    )
    app = Flask(__name__,
                instance_path=instance_path,
                instance_relative_config=True)
    
    app.config.from_object('cadastro.default_settings')
    app.config.from_pyfile('config.cfg')
    app.secret_key = app.config['SECRET_KEY']

    jwt = JWT(app, authenticate, identity)

    ### swagger implementacao ###
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'

    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': app.config['APP_NAMME'],
            "openapi": "3.0.1"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    ### fim da implementação do swagger ###
    
    api = Api(app)
    # Create API routes
    api.add_resource(Customer, '/api/Cliente', '/api/Cliente/<customer_id>')
    api.add_resource(Customers, '/api/Clientes')
    
    return app