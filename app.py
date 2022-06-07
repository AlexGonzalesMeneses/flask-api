import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from repository import Repository
from item import Item

app = Flask(__name__)
CORS(app)
items = Repository()


@app.get('/api/items')
def get_items():
    return items.get_items_to_json()


@app.post('/api/items')
def create_item():
    newItem = request.get_json()
    name = newItem['name']
    photo = newItem['photo']
    origen = newItem['origen']
    description = newItem['description']
    value = newItem['value']
    measureUnit = newItem['measureUnit']
    compositionMaterial = newItem['compositionMaterial']
    newItem = Item(items.get_next_id(), name, photo, origen,
                   description, value, measureUnit, compositionMaterial)
    items.insert(newItem)

    return newItem.toJSON()


@ app.put('/api/items/<item_id>')
def update_item(item_id):
    newItem = request.get_json()
    name = newItem['name']
    photo = newItem['photo']
    origen = newItem['origen']
    description = newItem['description']
    value = newItem['value']
    measureUnit = newItem['measureUnit']
    compositionMaterial = newItem['compositionMaterial']
    newItem = Item(item_id, name, photo, origen,
                   description, value, measureUnit, compositionMaterial)
    items.update(item_id, newItem)

    return newItem.toJSON()


@ app.delete('/api/items/<item_id>')
def delete_item(item_id):
    items.delete(item_id)
    return 'Delete succesfully', 204


@ app.get('/api/items/<item_id>')
def get_item(item_id):
    item = items.search(item_id)
    if item is None:
        return 'Item not found', 404
    return item.toJSON()


if __name__ == '__main__':
    app.run(debug=True)
