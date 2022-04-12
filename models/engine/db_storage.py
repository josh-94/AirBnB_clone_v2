#!/usr/bin/python3

'''This module supplies the `DBStorage` class
   that allows connecting to the database
'''
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

classes = [State, City, User, Place, Review, Amenity]


class DBStorage:
    '''DBStorage Class'''
    __engine = None
    __session = None

    def __init__(self):
        '''Creates the engine with the data of the user and database
        '''
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        mode = getenv('HBNB_ENV')

        url = "mysql+mysqldb://{}:{}@localhost/{}".format(user, pwd, db)
        self.__engine = create_engine(url, pool_pre_ping=True)

        if mode == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''Get the objects of the specified class

        Args:
            cls = class

        Return: dictionary of the objects of cls
        '''
        dict_obj = {}
        if cls is not None:
            result = self.__session.query(eval(cls))
            print(result)
            for obj in result:
                key = obj.__class__.__name__ + '.' + obj.id
                dict_obj[key] = obj

        else:
            for model in classes:
                try:
                    result = self.__session.query(model)
                except Exception:
                    break
                for obj in result:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dict_obj[key] = obj

        return (dict_obj)

    def new(self, obj):
        '''Adds the obj to the current database session'''
        self.__session.add(obj)

    def save(self):
        '''Commits all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Deletes from the current database session obj if not None'''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''Creates all tables in the database and
           the current database session
        '''
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
