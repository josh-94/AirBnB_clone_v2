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

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime(), default=datetime.utcnow())
    updated_at = Column(DateTime(), default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        '''Constructor'''
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    frmat = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, frmat))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''Method that represents the class object as a string'''

        if self.__dict__['_sa_instance_state'] is not None:
            del self.__dict__['_sa_instance_state']

        msg = "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id,
                                    str(self.__dict__))
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
        return (dic)

    def delete(self):
        '''Deletes the current instance'''
        models.storage.delete(self)
