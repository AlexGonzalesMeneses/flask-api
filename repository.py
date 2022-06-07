# lista de items
from item import Item
import json


class Repository:
    def __init__(self):
        self.items = [
            Item("1", "Coca Cola", "https://images.unsplash.com/photo-1567103472667-6898f3a79cf2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8Y29jYWNvbGElMjB8ZW58MHx8MHx8&w=1000&q=80",
                 "Mexico", "The Coke Company is a good drink", "1.00", "Litro", "Coca Cola"),
            Item("2", "Fanta", "https://cdn.shopify.com/s/files/1/0368/1363/5716/products/7771609001165_709x709.jpg?v=1637172460",
                 "Mexico", "The Coke Company is a good drink", "1.00", "Litro", "Coca Cola"),
            Item("3", "Sprite", "https://www.cocacola.es/content/dam/one/es/es2/sprite/home-page/sp-1-5-sp.jpg",
                 "Mexico", "The Coke Company is a good drink", "1.00", "Litro", "Coca Cola"),
        ]

    def search(self, id):
        for index, item in enumerate(self.items):
            if item.id == id:
                return self.items[index]
        return None

    def delete(self, id):
        self.items.remove(self.search(id))

    def update(self, id, new_item):
        for index, item in enumerate(self.items):
            if item.id == id:
                self.items[index] = new_item
                break

    def insert(self, new_item):
        self.items.append(new_item)

    def print_all(self):
        for item in self.items:
            print(item)

    def get_items_to_json(self):
        return json.dumps([item.__dict__ for item in self.items])

    def get_next_id(self):
        if len(self.items) == 0:
            return "1"
        else:
            return str(int(self.items[-1].id) + 1)
