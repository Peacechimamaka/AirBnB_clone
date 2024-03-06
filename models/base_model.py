#!/usr/bin/python3
"""This module contains the BaseModel Class
   The BaseModel Class should be inherited by all class in this project
   Because it contains all common attributes/methods for other classes
"""
import uuid
import datetime


class BaseModel:
    """BaseModel class for common attributes and methods"""
    def __init__(self):
        """Initializer method for BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.save()

    def __str__(self):
        """String representation of the BaseModel object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method to update the updated_at attribute with current timestamp"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Method to return a dictionary representation of the BaseModel"""
        custom_dict = self.__dict__
        # Add class name to new dictionary
        custom_dict.update({"__class__": self.__class__.__name__})
        # Retrieve created_at and updated_at values
        created_at_value = custom_dict['created_at']
        updated_at_value = custom_dict['updated_at']
        # Convert datetime objects to ISO format strings
        custom_dict['created_at'] = created_at_value.isoformat()
        custom_dict['updated_at'] = updated_at_value.isoformat()
        return custom_dict
