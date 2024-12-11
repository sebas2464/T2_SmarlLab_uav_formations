import requests

def arm_drone(drone_url):
    response = requests.get(f"{drone_url}/command/arm")
    if response.status_code != 200:
        raise Exception(f"erro ao armar o drone em {drone_url}. codigo: {response.status_code}")
    print(f"drone armado em {drone_url}.")

def takeoff_drone(drone_url, altitude):
    response = requests.get(f"{drone_url}/command/takeoff", params={"alt": altitude})
    if response.status_code != 200:
        raise Exception(f"erro ao decolar o drone em {drone_url}. codigo: {response.status_code}")
    print(f"drone decolou a {altitude}m em {drone_url}.")
####  
def get_drone_location(drone_url):
    response = requests.get(f"{drone_url}/telemetry/gps")
    if response.status_code != 200:
        raise Exception(f"erro ao obter localizacao do drone em {drone_url}. codigo: {response.status_code}")
    gps_data = response.json().get("info", {}).get("position", {})
    gps_data = {
        "lat": gps_data["lat"],
        "long": gps_data["lon"], 
        "alt": gps_data["alt"] - 584
    }
    print(f"localizacao do drone em {drone_url}: lat {gps_data['lat']}, long {gps_data['long']}, alt {gps_data['alt']}")
    return gps_data
