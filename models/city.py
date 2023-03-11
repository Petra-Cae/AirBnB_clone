#!/usr/bin/python3
from models.base_model import BaseModel
import uuid


class City(BaseModel):
    """updates city attributes"""
    state_id = ""
    name = ""
