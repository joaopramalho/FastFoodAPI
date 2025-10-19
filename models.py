from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

# connection with db
db = create_engine("sqlite:///database.db")

# base of the db
Base = declarative_base()

# create classes and tables
class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, default="John Doe")
    email = Column("email", String)
    password = Column("password", String)
    isActive = Column("isActive", Boolean, default=True)
    isAdmin = Column("isAdmin", Boolean, default=False)
    orders = Column("orders", ForeignKey)

    def __init__(self):
        

# execute the creation of the metadata