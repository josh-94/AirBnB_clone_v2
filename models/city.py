#!/usr/bin/python3

'''File with the class City'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    '''City Class'''
    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
