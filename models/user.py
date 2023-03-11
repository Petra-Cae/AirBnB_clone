#!/usr/bin/python3
""" for Class user"""
import uuid
from models.base_model import BaseModel


class User(BaseModel):
    """Store user data"""
    first_name = ""
    last_name = ""
    email = ""
    password = ""
