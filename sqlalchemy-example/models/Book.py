from sqlalchemy import Table, Column, Float, Integer, BigInteger, String, MetaData, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from models.base import Base
from models.Order import *
# association_table = Table('association', Base.metadata,
#     Column('book_id', Integer, ForeignKey('book.id')),
#     Column('order_id', Integer, ForeignKey('order.id'))
# )
class Book(Base):
    __tablename__ = "book"
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(16))
    # children = relationship("Order",
    #                 secondary=association_table)

    #children = relationship("Order", backref=backref("book", cascade="all, delete"))    

    #child = relationship("Order", backref="book", passive_deletes=True)