from flask import Flask, request
from flask_restful import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask (__name__)
api = Api(app)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate",
        "openapi": "3.0.1"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

items=[]

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
            return {'item':None},404
    
    def post(self,name):
        data = request.get_json()
        item = {'name':name, 'price':data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>') # htttp://localhost:5000/student/Rolf
api.add_resource(ItemList, '/items') # htttp://localhost:5000/student/Rolf

app.run(port=5000,debug=True)