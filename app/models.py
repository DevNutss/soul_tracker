# Database models
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#Setup the user table 
class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    national_id = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable = False)
    role = Column(String, default="patient" ) # could be patient or doctor


