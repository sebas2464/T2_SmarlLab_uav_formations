import requests

def move_follower_to_gps(follower_url, target_position):
    response = requests.post(f"{follower_url}/movement/go_to_gps/", json={
        "lat": target_position["lat"],
        "long": target_position["long"],  
        "alt": target_position["alt"]
    })
    if response.status_code != 200:
        raise Exception(f"Erro ao mover o seguidor para {target_position}. Código: {response.status_code}")
    print(f"Seguidor movido para {target_position}.")

def move_follower_to_ned(follower_url, target_position):
    response = requests.post(f"{follower_url}/movement/go_to_ned/", json={
        "x": target_position[0],
        "y": target_position[1],
        "z": target_position[2]
    })
    if response.status_code != 200:
        raise Exception(f"Erro ao mover o seguidor para {target_position}. Código: {response.status_code}")
    print(f"Seguidor movido para {target_position}.")
