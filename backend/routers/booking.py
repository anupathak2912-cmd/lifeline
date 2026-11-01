from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from services.fare import calculate_fare
from services.matching import find_nearest_ambulance_cell
from services.triage import evaluate_triage

router = APIRouter(prefix="/bookings", tags=["Bookings"])

class BookingRequest(BaseModel):
    lat: float
    lng: float
    symptoms: List[str]
    distance_km: float

@router.post("/")
def create_booking(data: BookingRequest):
    # 1. AI Triage evaluate karo symptoms ke base par
    triage_result = evaluate_triage(data.symptoms)
    ambulance_type = triage_result["recommended_ambulance"]
    
    # 2. Fixed fare calculate karo recommended ambulance ke hisab se
    fare = calculate_fare(data.distance_km, ambulance_type)
    
    # 3. H3 cell matching se nearest cells nikalo
    cells = find_nearest_ambulance_cell(data.lat, data.lng, ambulance_type)
    
    return {
        "status": "SUCCESS",
        "triage_analysis": triage_result,
        "estimated_fare": fare,
        "matched_h3_cells": cells[:3]
    }