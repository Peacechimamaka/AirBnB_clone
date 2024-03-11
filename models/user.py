#!/usr/bin/python3
'''Defines the class user'''
from base_model import BaseModel


class User(BaseModel):
    '''
    A class User.

    Attributes:

        email (str): The user's email.
        password : The user's password
        first_name: The first name of the user
        last_name: The last name of the user
        '''

    email = " "
    password = " "
    first_name = " "
    last_name = " "
