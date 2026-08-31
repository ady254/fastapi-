# What is the purpose of this file i.e. models.py?
# this file defines the data validation schema using Pydantic
# by inheriting the from "BaseModel", the "Product class" acts as a strict rule of our api request and responses it ensures that whenever a client creates or updates a product, 
# the data must matches this validations like id should be integer name string etc...
# if user sends a invalid data like price in string instead of integer , fastapi automatically catch it and return 422 validation error

from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
