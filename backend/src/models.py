from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class List(Base):
    __tablename__ = "lists"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    
    links = relationship("Link", back_populates="list")

class Link(Base):
    __tablename__ = "links"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(500), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    list_id = Column(Integer, ForeignKey("lists.id"), nullable=True)
    
    list = relationship("List", back_populates="links")