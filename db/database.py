from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base= declarative_base() #parent class
engine = create_engine("sqlite:///expense.db") #engine for db
SessionLocal = sessionmaker(bind=engine) #indivual session for dtata collection

def init_db():
    """Initialize the database by creating tables"""
    Base.metadata.create_all(bind=engine)
