#!/usr/bin/python3

'''File with the class State'''
from os import getenv
import models
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
            cities = models.storage.all('City')
            list_city = []
            for city in cities.values():
                if city.state_id == self.id:
                    list_city.append(city)
            return (list_city)
