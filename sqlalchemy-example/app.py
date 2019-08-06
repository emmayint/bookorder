from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.Book import *
from models.Order import *

engine = create_engine('mysql://root:cc7alembic@localhost:3306/bookorder', echo=False)
Base.metadata.create_all(bind=engine)
# create a configured "Session" class
Session = sessionmaker(bind=engine)
# create a Session
session = Session()
try:
    book = Book()
    book.id = 3
    book.title = 'mariadb'
    session.add(book)
    session.flush()
    try:
        with session.begin_nested():
            #session.begin_nested()
            order = Order()
            order.id = 1
            order.quantity = 58
            order.book_id = 3
            session.add(order)
    except:
        #session.rollback()
        print('cannot add order')
except:
    session.rollback()
    print('cannot add book')
    raise
finally:
    session.commit()
    session.close()