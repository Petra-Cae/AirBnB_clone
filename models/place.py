#!/usr/bin/python3
"""Define the class Place"""

from models.base_model import BaseModel
import uuid


class Place(BaseModel):
    """Store Place attributes"""
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    amenity_ids = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
