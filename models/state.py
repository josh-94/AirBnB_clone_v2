#!/usr/bin/python3

'''File with the class State'''
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

storage = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    '''State Class'''
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if storage == 'db':
        cities = relationship('City', backref='state')

    else:
        @property
        def cities(self):
            return (0)
