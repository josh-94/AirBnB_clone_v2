#!/usr/bin/python3

'''File with the class Place'''
import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

storage = getenv('HBNB_TYPE_STORAGE')


class Place(BaseModel, Base):
    '''Place Class'''
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True, default='NULL')
    number_rooms = Column(Integer(), nullable=False, default=0)
    number_bathrooms = Column(Integer(), nullable=False, default=0)
    max_guest = Column(Integer(), nullable=False, default=0)
    price_by_night = Column(Integer(), nullable=False, default=0)
    latitude = Column(Float(), nullable=True, default=0.000)
    longitude = Column(Float(), nullable=True, default=0.000)
    amenity_ids = []

    reviews = relationship('Review', backref='place')

    if storage != 'db':
        @property
        def reviews(self):
            reviews = models.storage.all('Review')
            list_review = []
            for review in reviews.values():
                if review.place_id == self.id:
                    list_review.append(review)
            return (list_review)
