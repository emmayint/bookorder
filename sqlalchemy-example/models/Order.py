from sqlalchemy import Table, Column, Float, Integer, BigInteger, String, MetaData, DateTime, ForeignKey, Enum
from sqlalchemy.orm import backref
from models.Book import *
from models.base import Base
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = "order"
    id = Column('id', Integer, primary_key=True)
    quantity = Column('quantity', Integer)
    book_id = Column('book_id', Integer, ForeignKey('book.id', onupdate="CASCADE", ondelete='CASCADE'))
