#!/usr/bin/python3
"""test for file storage"""
import unittest
import MySQLdb
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'DB')
class TestDBStorage(unittest.TestCase):
    '''this will test the FileStorage'''

    def test_dbStorage(self):
        '''Test existence of database'''
        pass

