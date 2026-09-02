#In this code, we are building a basic backend REST API using FASTAPI in python, we are managing a mock product inventory store in temporarily in a python list
from fastapi import Depends, FastAPI
from models import Product
from config import Session, engine  # import database configuration from config.py
import database   # database models (from database.py).

app = FastAPI()
database.Base.metadata.create_all(bind=engine) # acts as an automated table creation step on startup

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

def get_db():     # session close
    db = Session()
    try:
        yield db
    finally:
        db.close()



#this is a database seeding function. When the application starts up or needs initial test data, init_db opens a database session, iterates through our mock products list, converts each Pydantic model into a dictionary using .model_dump(), and instantiates our SQLAlchemy Product model.
# Finally, it stages those records using db.add() and persists them to the PostgreSQL database in a single transaction using db.commit().

def init_db():     # written function to commit data into database by mapping the sqlalchemy

    db = Session()
    count = db.query(database.Product).count
    if count == 0:

       for product in products:
            db.add(database.Product(**product.model_dump()))  #product.model_dump(): Converts the Pydantic product model into a standard Python dictionary. (Note: In older versions of Pydantic, this was .dict()). 
                                                         # ** (Double Asterisk): Unpacks that dictionary into keyword arguments.
                                                         # database.Product(...): Creates a SQLAlchemy database model instance using those unpacked values. db.add(...): Stages this new product record into the current session queue, telling SQLAlchemy it's ready to be written to the database. 
        
       db.commit()
init_db()

# logic for fetching all the products
@app.get("/products")       # GET endpoint retrieves and returns the entire list of products stored in the products array
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database.Product).all()

   
    return db_products
# fetch by id
@app.get("/product/{id}") 
def get_product_by_id(id: int, db: Session = Depends(get_db)):   # here GET endpoint use a dynamic path parameter (id). It iterates through the products list, 
                              # looks product whose ID matches the requested integer, and return that specific product
    db_product = db.query(database.Product).filter(database.Product.id == id).first()
    if db_product:  
         return db_product
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


    

