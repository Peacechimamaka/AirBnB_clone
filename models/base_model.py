#!/usr/bin/python3
"""
   This module contains the BaseModel Class
   The BaseModel Class should be inherited by all class in this project
   Because it contains all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """BaseModel class for common attributes and methods"""
    def __init__(self, *args, **kwargs):
        """Initializer method for BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                # convert the created_at value from string to datetime object
                DateFormat = "%Y-%m-%dT%H:%M:%S.%f"
                if key == 'created_at':
                    value = datetime.strptime(kwargs['created_at'], DateFormat)

                # convert the created_at value from string to datetime object
                if key == 'updated_at':
                    value = datetime.strptime(kwargs['updated_at'], DateFormat)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """String representation of the BaseModel object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method to update the updated_at attribute with current timestamp"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Method to return a dictionary representation of the BaseModel"""
        custom_dict = {}
        for key, value in self.__dict__.items():
            custom_dict.update({key: value})
        # Add class name to new dictionary
        custom_dict.update({"__class__": self.__class__.__name__})
        # Retrieve created_at and updated_at values
        created_at_value = custom_dict['created_at']
        updated_at_value = custom_dict['updated_at']
        # Convert datetime objects to ISO format strings
        custom_dict['created_at'] = created_at_value.isoformat()
        custom_dict['updated_at'] = updated_at_value.isoformat()
        return custom_dict
