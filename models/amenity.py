#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
