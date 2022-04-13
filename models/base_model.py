#!/usr/bin/python3

'''File with the `BaseModel` Class'''

import uuid
from datetime import datetime
import models

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

Base = declarative_base()


class BaseModel:
    '''BaseModel Class'''

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        '''Constructor'''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    frmat = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, frmat))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        '''Method that represents the class object as a string'''

        dict_attr = self.__dict__.copy()
        if '_sa_instance_state' in dict_attr:
            del dict_attr['_sa_instance_state']
        msg = "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id,
                                    str(dict_attr))
        return (msg)

    def save(self):
        '''Saves the object in the database'''
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values
        of __dict__ of the instance'''
        dic = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dic[key] = str(value.isoformat())
            else:
                dic[key] = value
        dic["__class__"] = self.__class__.__name__
        if '_sa_instance_state' in dic:
            del dic['_sa_instance_state']
        return (dic)

    def delete(self):
        '''Deletes the current instance'''
        models.storage.delete(self)
