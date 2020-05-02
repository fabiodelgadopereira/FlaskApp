# coding: utf-8
from os import path
from flask import Flask
from .resources.cliente import cliente_blueprint




def create_app(mode):
    instance_path = path.join(
        path.abspath(path.dirname(__file__)), "%s_instance" % mode
    )
    app = Flask(__name__,
                instance_path=instance_path,
                instance_relative_config=True)
    
    app.config.from_object('cadastro.default_settings')
    app.config.from_pyfile('config.cfg')

    app.config['MEDIA_ROOT'] = path.join(
        app.config.get('PROJECT_ROOT'),
        app.instance_path
    )
    
    cliente_blueprint.run(debug=True) 
    
    
    return app