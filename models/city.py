#!/usr/bin/python3
"""
This module contains the definition of the City class, which represents
an city in an Airbnb clone project.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A class representing a city in an Airbnb clone project.
    """
    state_id = ""
    name = ""

    def __str__(self):
        """
        Return a string representation of the City object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
