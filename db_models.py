from sqlalchemy import Column, Integer, String
from database import Base

class StudentDB(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    career = Column(String(50))