import json


class Item:
    def __init__(self, id, name, photo, origen, description, value, measureUnit, compositionMaterial):
        self.id = id
        self.name = name
        self.photo = photo
        self.origen = origen
        self.description = description
        self.value = value
        self.measureUnit = measureUnit
        self.compositionMaterial = compositionMaterial

    def __str__(self):
        return f"{self.name} - {self.description}"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
