#!/usr/bin/python3
"""JSON """
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FIleStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the new objects"""
        nobj = obj.__class__.__name__
        FileStorage.__objects["{}{}".format(nobj, obj.id)] = obj

    def save(self):
        """Serializes objects to the JSON file"""
        uject = FileStorage.__objects
        udt = {obj: uject[obj].to_dict()}
        with open(FileStorage.__file_path, "w") as f:
            udt = {}
            udt.update(FileStorage.__objects)
            for k, v in udt.items():
                udt[k] = v.to_dict()
            json.dump(udict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                udt = json.load(f)
                for obj in udt.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
