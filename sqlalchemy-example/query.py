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

#session.query(Order).filter(Order.book_id == 3).delete()
#session.query(Book).filter(Book.id == 3).delete()

# books = session.query(Book).all()
# for book in books:
#     print("Book id is %s and titile is %s" % (book.id, book.title))

# orders = session.query(Order).all()
# for order in orders:
#     print("Order id is %s, %s copies of book_id %s" % (order.id, order.quantity, order.book_id))

for b, o in session.query(Book, Order).filter(Book.id == Order.book_id).all():
   print ("book ID: {}, title: {}, order No: {}, quantity: {}".format(b.id,b.title, o.id, o.quantity))

results = session.query(Book, Order).join(Book, Book.id == Order.book_id).filter(Book.id == 1)
for result in results:
    print('Book Title: {}, order quantity: {}' .format(result[0].title, result[1].quantity))

session.commit()
session.close()