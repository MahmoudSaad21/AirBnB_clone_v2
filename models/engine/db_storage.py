#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import urllib.parse

from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class DBStorage:
    """This class manages storage of hbnb models in a SQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the SQL database storage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        session = self.__session
        obj_dict = {}
        if cls:
            objs = session.query(eval(cls)).all()
            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[key] = obj
        else:
            for name in models.classes:
                objs = session.query(models.classes[name]).all()
                for obj in objs:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    obj_dict[key] = obj
        return obj_dict
    
    def new(self, obj):
        """Adds new object to storage database"""
        self.__session.add(obj)

    def save(self):
        """Commits the session changes to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Removes an object from the storage database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                      expire_on_commit=False))
        self.__session = scoped_session(SessionFactory)()
