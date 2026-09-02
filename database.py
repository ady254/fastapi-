#In database.py, I'm using SQLAlchemy's declarative base to map a Python class called Product to a PostgreSQL table. 
# I've defined the columns with their respective data types—like Integers, Strings, and Floats—and set up constraints like a primary key and index on the ID for performance.
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()   # create a base class.  Every database model you write will inherit from this Base, allowing SQLAlchemy to track and map your Python classes to actual SQL tables.

class Product(Base):        # Defines a model named Product that represents a table in your PostgreSQL database.

    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True )
    name = Column(String)
    price = Column(Float)
    description = Column(String)
    quantity = Column (Integer)


