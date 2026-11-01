from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
import models
from services.triage import evaluate_triage
from services.fare import calculate_fare
from services.matching import find_nearest_ambulance_cell

router = APIRouter(prefix="/bookings", tags=["Bookings"])

class BookingRequest(BaseModel):
    lat: float
    lng: float
    symptoms: str
    distance_km: float

@router.post("/")
def create_booking(req: BookingRequest, db: Session = Depends(get_db)):
    # 1. Triage evaluation (Critical vs Moderate)
    triage_res = evaluate_triage(req.symptoms)
    needed_type = triage_res["ambulance_type"]

    # 2. Fare calculation
    fare = calculate_fare(req.distance_km, needed_type)

    # 3. Find nearby H3 cells for ambulance matching
    matched_cells = find_nearest_ambulance_cell(req.lat, req.lng, needed_type)

    # 4. Save booking record to SQLite database
    new_booking = models.BookingModel(
        lat=req.lat,
        lng=req.lng,
        symptoms=req.symptoms,
        triage_level=triage_res["triage_level"],
        ambulance_type=needed_type,
        estimated_fare=fare
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    # 5. Return complete response with Booking ID
    return {
        "booking_id": new_booking.id,
        "status": "CONFIRMED",
        "triage": triage_res,
        "estimated_fare": fare,
        "matched_h3_cells": matched_cells
    }