# lista de items
from item import Item
import json


class Repository:
    def __init__(self):
        self.items = [
            Item("1", "Coca Cola", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/15-09-26-RalfR-WLC-0098.jpg/320px-15-09-26-RalfR-WLC-0098.jpg",
                 "Mexico", "The Coke Company is a good drink", "1.00", "Litro", "Coca Cola"),
            Item("2", "Fanta", "https://www.cocacola.com.mx/content/dam/coke/images/coca-cola/coca-cola-logo-1.png",
                 "Mexico", "The Coke Company is a good drink", "1.00", "Litro", "Coca Cola"),
            Item("3", "Sprite", "https://www.cocacola.com.mx/content/dam/coke/images/coca-cola/coca-cola-logo-1.png",
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
