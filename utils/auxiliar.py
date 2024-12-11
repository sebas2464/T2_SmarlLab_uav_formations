import math

def ned_to_gps(base_gps, ned_offset):
    meters_to_lat = ned_offset[0] / 111320
    meters_to_lon = ned_offset[1] / (111320 * abs(math.cos(math.radians(base_gps["lat"]))))
    return {
        "lat": base_gps["lat"] + meters_to_lat,
        "long": base_gps["long"] + meters_to_lon, 
        "alt": base_gps["alt"] + ned_offset[2]
    }

def gps_distance(point1, point2):
    lat_diff = (point2["lat"] - point1["lat"]) * 111320
    lon_diff = (point2["long"] - point1["long"]) * 111320 * abs(math.cos(math.radians(point1["lat"])))  
    alt_diff = point2["alt"] - point1["alt"]
    return math.sqrt(lat_diff**2 + lon_diff**2 + alt_diff**2)
