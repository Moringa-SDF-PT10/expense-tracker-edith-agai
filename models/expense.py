from sqlalchemy import Column, Integer, String, Float, Date
from db.database import Base

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String)

    def __repr__(self):
        return f"<Expense(name='{self.name}', amount={self.amount})>"