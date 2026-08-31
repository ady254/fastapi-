#In this code, we are building a basic backend REST API using FASTAPI in python, we are managing a mock product inventory store in temporarily in a python list
from fastapi import FastAPI
from models import Product
from config import Session, engine
import database

app = FastAPI()
database.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to Alein Store"

#greet()

products = [
    Product(id=1, name="phone", description= "A smartphone build next-gen ai features", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description= "A powerful laptop", price=999.99, quantity=30),
    Product(id=6, name="Magic Lazor", description= "A blue lazor", price=119.99, quantity=10),
    Product(id=4, name="study table", description= "A long lasting study table", price=399.99, quantity=12),
]

# logic for fetching all the products
@app.get("/products")       # GET endpoint retrieves and returns the entire list of products stored in the products array
def get_all_product():
    db = session()
    db.query()   
    return products
# fetch by id
@app.get("/product/{id}") 
def get_product_id(id: int):   # here GET endpoint use a dynamic path parameter (id). It iterates through the products list, 
                              # looks product whose ID matches the requested integer, and return that specific product
    for product in products:  
        if product.id == id:  
            return product
    return "products not found"  # if no match is found it returns "products not found"


# add a new product in our Product list
@app.post("/product")            
def add_product(product: Product):   # here POST endpoint use to create a new resource/product, it takes a request body validate against the "Product" schema/class, 
    products.append(product)         # appends it our products list, and return the newly added product back to the client
    return product
# update product logic
@app.put("/product")
def update_product(id: int, product: Product):  # PUT endpoint use to update the product, it takes a request body validate against the "Product" schema
    for i in range(len(products)):             # iterates the products list, matches with product ID and update those product by return product added sccessfully
        if products[i].id == id:
            products[i] = product
            return "Product Added Successfully"
    return "No product found"                   # if no matche is found it returns product not found


# delete product logic
@app.delete("/product")            
def delete_product(id: int):     #DELETE endpoint uses to delete the product,it iterates through the product list, looks product whose id matches the requested int and delete the product and return "Product deleted"
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"


    

