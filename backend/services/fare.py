def calculate_fare(distance_km: float, ambulance_type: str) -> int:
    """
    Calculates fixed-fare based on distance and ambulance type.
    """
    base_fares = {
        "BLS": 500,
        "ALS": 1000,
        "TRANSPORT": 400,
        "NEONATAL": 1200
    }
    per_km_rates = {
        "BLS": 20,
        "ALS": 35,
        "TRANSPORT": 15,
        "NEONATAL": 40
    }
    
    ambulance_type = ambulance_type.upper()
    b_fare = base_fares.get(ambulance_type, 500)
    km_rate = per_km_rates.get(ambulance_type, 20)
    
    total_fare = b_fare + (distance_km * km_rate)
    return int(round(total_fare))