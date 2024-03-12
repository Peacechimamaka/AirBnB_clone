#!/usr/bin/python3
"""
This module provides unit tests for the Place class.
"""
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """
    TestPlace class provides unit tests for the Place class.
    """
    def setUp(self):
        """
        setUp method initializes a Place instance for each test.
        """
        self.instance = Place()

    def test_types(self):
        """
        Test the types of all attributes
        """
        self.assertEqual(type(self.instance), Place)
        self.assertEqual(type(self.instance.city_id), str)
        self.assertEqual(type(self.instance.user_id), str)
        self.assertEqual(type(self.instance.name), str)
        self.assertEqual(type(self.instance.description), str)
        self.assertEqual(type(self.instance.number_rooms), int)
        self.assertEqual(type(self.instance.number_bathrooms), int)
        self.assertEqual(type(self.instance.max_guest), int)
        self.assertEqual(type(self.instance.price_by_night), int)
        self.assertEqual(type(self.instance.latitude), float)
        self.assertEqual(type(self.instance.longitude), float)
        self.assertEqual(type(self.instance.amenity_ids), list)

    def test_default_value(self):
        """
        Tests the default value of all attributes
        """
        self.assertEqual(self.instance.city_id, "")
        self.assertEqual(self.instance.user_id, "")
        self.assertEqual(self.instance.name, "")
        self.assertEqual(self.instance.description, "")
        self.assertEqual(self.instance.number_rooms, 0)
        self.assertEqual(self.instance.number_bathrooms, 0)
        self.assertEqual(self.instance.max_guest, 0)
        self.assertEqual(self.instance.price_by_night, 0)
        self.assertEqual(self.instance.latitude, 0.0)
        self.assertEqual(self.instance.longitude, 0.0)
        self.assertEqual(self.instance.amenity_ids, [])

    def test_custom_values(self):
        """
        Change the default value and Test
        """
        self.instance.name = "Apartment"
        self.assertEqual(self.instance.name, "Apartment")
        self.instance.description = "A small place you can call home"
        self.assertEqual(self.instance.description, "A small place you can "
                                                    "call home")
        self.instance.number_rooms = 4
        self.assertEqual(self.instance.number_rooms, 4)
        self.instance.number_bathrooms = 6
        self.assertEqual(self.instance.number_bathrooms, 6)
        self.instance.max_guest = 7
        self.assertEqual(self.instance.max_guest, 7)
        self.instance.price_at_night = 110000
        self.assertEqual(self.instance.price_at_night, 110000)
        self.instance.latitude = 802.782
        self.assertEqual(self.instance.latitude, 802.782)
        self.instance.longitude = 567.456
        self.assertEqual(self.instance.longitude, 567.456)
