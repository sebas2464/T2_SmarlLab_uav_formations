import os
import time
from argparse import ArgumentParser
from protocol_testing import launch_protocol_testing
from utils.api import get_drone_location, arm_drone, takeoff_drone
from utils.formations import FORMATIONS
from leader_control.leader import move_leader_to_gps
from follower_control.follower import move_follower_to_gps
from utils.aux import ned_to_gps, gps_distance
import requests

def wait_to_followers(leader_position, followers, proximity=20):
    print("Esperando a que os followers estejam perto do lider...")
    while True:
        all_followers_close = True
        for i in range(len(followers)):
            follower_url = followers[i]

            follower_position = get_drone_location(follower_url)
            distance_to_leader = gps_distance(leader_position, follower_position)
            print(f"Seguidor {i} esta a {distance_to_leader:.2f} metros do lider.")
            if distance_to_leader > proximity:
                all_followers_close = False
        
        if all_followers_close:
            print("Todos os seguidores estao pertos do lider.")
            break

        time.sleep(1)




def wait_for_server(url, timeout=30):
    start_time = time.time()
    while True:
        try:
            response = requests.get(f"{url}/telemetry/gps")
            if response.status_code == 200:
                print(f"Servidor em {url} esta pronto.")
                return
        except requests.ConnectionError:
            pass

        if time.time() - start_time > timeout:
            raise Exception(f"Timeout ao esperar pelo servidor em {url}.")
        
        print(f"Esperando servidor em {url}...")
        time.sleep(1)

def main():
    parser = ArgumentParser()
    parser.add_argument('--n', type=int, default=3, help="Número de drones na formação")
    parser.add_argument('--formation', type=str, default="square", help="Formacão inicial dos drones")
    args = parser.parse_args()

    # Lançar os drones e configurar as URLs
    print("Lanzando os drones configurados com os parametros definidos...")
    leader_url, followers = launch_protocol_testing(args)

    # Esperar servidores
    print("Esperando que os servidores dos drones estejam prontos...")
    wait_for_server(leader_url)
    for follower_url in followers:
        wait_for_server(follower_url)

    # Configurar o líder
    print("Armando e iniciando o líder...")
    arm_drone(leader_url)
    takeoff_drone(leader_url, altitude=50)
    leader_position = get_drone_location(leader_url)
    print(f"Posisao inicial do líder: {leader_position}")

    # Configurar os seguidores: armar e decolar
    print("Armando e iniciando os seguidores...")
    for follower_url in followers:
        arm_drone(follower_url)
        takeoff_drone(follower_url, altitude=50)
        print(f"Seguidor em {follower_url} armado e decolado.")

    # Configurar os seguidores na formação inicial
    formation_function = FORMATIONS[args.formation] 
    formation_positions = formation_function(args.n - 1) 
    print("Configurando os seguidores na formação inicial...")
    for i in range(len(followers)):
        follower_url[i]
        relative_position = formation_positions[i]
        follower_target = ned_to_gps(leader_position, relative_position)
        print(f"Seguidor {i} indo para a posisao inicial: {follower_target}")
        move_follower_to_gps(follower_url, follower_target)
    time.sleep(10)

    # Executar a missão
    route = [{"lat": -35.3635289, "long": 149.1645755, "alt": 50},{"lat": -35.3635956, "long": 149.1657342, "alt": 50},{"lat": -35.3628629, "long": 149.1651106, "alt": 50}]

    print("iniciando a missão com o líder...")
    for waypoint in route:
        print(f"Líder indo para o waypoint: {waypoint}")
        move_leader_to_gps(leader_url, waypoint)

        while True:
            leader_position = get_drone_location(leader_url)
            distance_to_waypoint = gps_distance(leader_position, waypoint)
            print(f"Distancia até o waypoint: {distance_to_waypoint:.2f} metros")

            if distance_to_waypoint < 2.0:
                print("Líder chegou ao waypoint/ esperando followers")
                for i in range(len(followers)):
                    follower_url = followers[i]
                    
                    relative_position = formation_positions[i]
                    print(f"**")
                    print(f"´posicion relativa  follower {i} es : {relative_position}")
                    follower_target = ned_to_gps(leader_position, relative_position)
                    print(f"Ajustando follower {i} para a posicao: {follower_target}")
                    move_follower_to_gps(follower_url, follower_target)   
                    print("__________________________________________________________________")  
                wait_to_followers(leader_position, followers)
                break

            for i in range(len(followers)):
                follower_url = followers[i]
                
                relative_position = formation_positions[i]
                print(f"**")
                print(f"´posicion relativa  follower {i} es : {relative_position}")
                follower_target = ned_to_gps(leader_position, relative_position)
                print(f"Ajustando follower {i} para a posicao: {follower_target}")
                move_follower_to_gps(follower_url, follower_target)
            print("__________________________________________________________________")  
            print("__________________________________________________________________")       
            time.sleep(15)
    print("Missão concluida com sucesso!")

if __name__ == "__main__":
    main()


### puse comentarios is moving en api.py o arducopter -auv:control/routers/movement