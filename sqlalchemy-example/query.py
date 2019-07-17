from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Float, Integer, BigInteger, String, MetaData, DateTime, ForeignKey, Enum
from sqlalchemy.orm import sessionmaker, relationship
from models.Book import *
from models.Order import *

#Base = declarative_base()

# an Engine, which the Session will use for connection # resources
engine = create_engine('mysql://root:cc7alembic@localhost:3306/bookorder', echo=True)
Base.metadata.create_all(bind=engine)
# create a configured "Session" class
Session = sessionmaker(bind=engine)
# create a Session
session = Session()

#session.query(Order).filter(Order.book_id == 1).delete()
session.query(Book).filter(Book.id == 1).delete()

books = session.query(Book).all()
for book in books:
    print("Book id is %s and titile is %s" % (book.id, book.title))

orders = session.query(Order).all()
for order in orders:
    print("Order id is %s and book_id is %s" % (order.id, order.book_id))

session.commit()
session.close()