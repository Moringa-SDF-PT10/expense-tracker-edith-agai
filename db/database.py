from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

base= declarative_base()
engine = create_engine("sqlite:///expense.db")
SessionLocal = sessionmaker(bind=engine)