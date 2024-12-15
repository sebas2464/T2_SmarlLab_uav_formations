import requests

def move_leader_to_gps(leader_url, waypoint):
    response = requests.post(f"{leader_url}/movement/go_to_gps/", json={
        "lat": waypoint["lat"],
        "long": waypoint["long"],  
        "alt": waypoint["alt"]
    })
    if response.status_code != 200:
        raise Exception(f"Erro ao mover o líder para {waypoint}. Código: {response.status_code}")
    print(f"Líder movido para {waypoint}.")


def move_leader_to_ned(leader_url, waypoint):
    response = requests.post(f"{leader_url}/movement/go_to_ned/", json={
        "x": waypoint[0],
        "y": waypoint[1],
        "z": waypoint[2]
    })
    if response.status_code != 200:
        raise Exception(f"Erro ao mover o líder para {waypoint}. Código: {response.status_code}")
    print(f"Líder movido para {waypoint}.")
