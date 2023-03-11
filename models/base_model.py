#!/usr/bin/python3
"""
Defines the class BaseModel which defines all common attributes
for all other classes in the AirBnB
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all methods for other classes in the AirBnB project"""
    def __init__(self, *args, **kwargs):
        """
        Initializes BaseModel
        Args:
            *args: unused
            **kwargs(dict): key/value pair of attributes
        """
        usrft = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for ukey, uval in kwargs.items():
                if ukey == "created_at" or ukey == "update_at":
                    self.__dict__[ukey] = datetime.strptime(uval, usrft)
                else:
                    self.__dict__[ukey] = uval
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates 'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        nusr = self.__class.__name__
        return "[{}] ({}) {}".format(nusr, self.id, self.__dict__)

    def to_dict(self):
        """
        return dictionary containing all keys/values of __dict__ of instance
        """
        udict = {}
        udict = self.__dict__.copy()
        udict["__class__"] = self.__class__.__name__
        udict["created_at"] = self.created_at.isoformat()
        udict["updated_at"] = self.updated_at.isoformat()
        return udict
