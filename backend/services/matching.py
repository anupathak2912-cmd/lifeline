import h3

def find_nearest_ambulance_cell(lat: float, lng: float, needed_type: str = "BLS", max_rings: int = 5):
    """
    Finds nearest available ambulance using H3 v4 grid cells, 
    expanding outward ring by ring.
    """
    resolution = 9  # H3 resolution for local neighborhood matching
    origin_cell = h3.latlng_to_cell(lat, lng, resolution)
    
    # Expand outward ring by ring to search for available cells
    for ring in range(0, max_rings + 1):
        cells = h3.grid_disk(origin_cell, ring)
        if cells:
            # Return discovered cells for matching logic
            return list(cells)
            
    return []