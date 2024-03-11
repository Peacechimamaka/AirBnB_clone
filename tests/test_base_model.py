#!/usr/bin/python3
"""
    This module provides unit tests for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
import datetime
import time


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class provides unit tests for the BaseModel class.
    """
    def setUp(self):
        """
        setUp method initializes a BaseModel instance for each test.
        """
        self.instance = BaseModel()
        self.instance.number = 89

    def test_id(self):
        """
        Test if the id attribute is of type str and
        number attribute is of type int.
        """
        self.assertIsInstance(self.instance.id, str)
        self.assertIsInstance(self.instance.number, int)

    def test_created_at(self):
        """
        Test if the created_at attribute is an instance of datetime.datetime.
        """
        self.assertIsInstance(self.instance.created_at, datetime.datetime)

    def test_updated_at(self):
        """
        Test if the updated_at attribute is an instance of datetime.datetime.
        """
        self.assertIsInstance(self.instance.updated_at, datetime.datetime)

    def test_str(self):
        """
        Test if the __str__() method returns the expected string representation
        """
        i_dict = f"[BaseModel] ({self.instance.id}) {self.instance.__dict__}"
        self.assertEqual(self.instance.__str__(), i_dict)

    def test_save(self):
        """
        Test if the save() method updates the updated_at attribute correctly.
        """
        updated_at_value = self.instance.updated_at
        time.sleep(10)
        new_time = updated_at_value + datetime.timedelta(seconds=10)
        self.instance.save()
        self.assertEqual(new_time.replace(microsecond=0),
                         self.instance.updated_at.replace(microsecond=0))

    def test_to_dict(self):
        """
        Test if the to_dict() method returns a dictionary
        with expected keys and values
        """
        instance_dict = self.instance.to_dict()
        self.assertIn('__class__', instance_dict)
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)
        self.assertIn('number', instance_dict)
        self.assertIsInstance(instance_dict['id'], str)
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)
        self.assertIsInstance(instance_dict['__class__'], str)
        self.assertIsInstance(instance_dict['number'], int)
