#!/usr/bin/python3
""" class reviews for the BnB"""
import uuid
from models.base_model import BaseModel


class Review(BaseModel):
    """Stores reviews to the BnB"""
    user_id = ""
    place_id = ""
    text = ""
