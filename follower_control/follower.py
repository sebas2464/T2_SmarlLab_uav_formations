    import requests

def move_follower(follower_url, leader_position, offset):
    """Ajusta la posición del seguidor relativo al líder."""
    target_position = {
        "x": leader_position["x"] + offset[0],
        "y": leader_position["y"] + offset[1],
        "z": leader_position["z"]
    }
    response = requests.get(f"{follower_url}/movement/go_to_ned", params=target_position)
    if response.status_code != 200:
        raise Exception(f"Error al mover el seguidor. Código: {response.status_code}")
    print(f"Seguidor movido a {target_position}.")
