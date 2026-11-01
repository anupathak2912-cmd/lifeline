from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String, unique=True, index=True)
    role = Column(String) # patient, driver, hospital, admin

class Ambulance(Base):
    __tablename__ = "ambulances"
    id = Column(Integer, primary_key=True, index=True)
    reg_no = Column(String)
    type = Column(String) # TRANSPORT, BLS, ALS, NEONATAL
    status = Column(String, default="FREE") # FREE, BUSY, OFFLINE
    lat = Column(Float)
    lng = Column(Float)
    h3_cell = Column(String) 
    
    from sqlalchemy import Column, Integer, String, Float
from database import Base

class BookingModel(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    symptoms = Column(String, nullable=False)
    triage_level = Column(String, nullable=False)  # Critical or Moderate
    ambulance_type = Column(String, nullable=False)  # ALS or BLS
    estimated_fare = Column(Integer, nullable=False)