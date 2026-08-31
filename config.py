#This file is responsible for setting up the database connection layer using SQLAlchemy.
#It defines the PostgreSQL connection URL, creates the database engine, and configures a SessionLocal factory. I use sessionmaker with autocommit=False so that database transactions are handled safely and explicitly within our API routes.

from sqlalchemy import create_engine    #Imports SQLAlchemy tools required to connect Python to a database and manage database transactions (sessions).
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:yourpassword@localhost:5432/underdog" #
engine = create_engine(db_url)   # Establishes the core interface (the "engine") that communicates with PostgreSQL database.
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # creates a configured factory class for database sessions

