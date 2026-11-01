def calculate_fare(distance_km: float, ambulance_type: str) -> int:
    # Base rates according to ambulance type
    rates = {
        "TRANSPORT": {"base": 400, "base_km": 5, "per_km": 12},
        "BLS": {"base": 700, "base_km": 5, "per_km": 15},
        "ALS": {"base": 1500, "base_km": 5, "per_km": 25},
        "NEONATAL": {"base": 2000, "base_km": 5, "per_km": 30}
    }
    
    rate = rates.get(ambulance_type, rates["BLS"])
    base_fare = rate["base"]
    base_km = rate["base_km"]
    per_km_rate = rate["per_km"]
    
    if distance_km <= base_km:
        total_fare = base_fare
    else:
        extra_km = distance_km - base_km
        total_fare = base_fare + (extra_km * per_km_rate)
        
    return int(round(total_fare))

import h3

def find_nearest_ambulance_cell(lat: float, lng: float, needed_type: str):
    # Convert latitude and longitude to H3 cell index (Resolution 8)
    cell = h3.latlng_to_cell(lat, lng, res=8)
    
    # Expand search ring by ring (0 to 5)
    for ring in range(0, 6):
        cells = list(h3.grid_disk(cell, ring))
        return cells
    return []