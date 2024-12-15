import os
import requests

def launch_protocol_testing(args):
    leader_url = None
    followers = []

    for i in range(args.n):
        connection = f"127.0.0.1:17{171 + i}" 
        port = 8000 + i 
        sysid = 40 + i  
        location = "0,0,0"  
        speed_leader = 1
        speed_follower = 3
        uav_speed = 0

        if i == 0:
            speed_command = speed_leader    
        else:
            speed_command = speed_follower
            

        #  --protocol foi deletado daqui
        uav_command = (
            f"python3.10 ~/uav_control/uav_api.py --simulated true --sysid {sysid} "
            f"--uav_connection {connection} --port {port} --speedup {speed_command} "
            f"--gs_connection 172.27.224.1:14550 &" 
        )      # deberia conetar ao mission planer supostamente# 172.27.224.1
        os.system(uav_command)

        if i == 0:
            leader_url = f"http://localhost:{port}" 
        else:
            followers.append(f"http://localhost:{port}") 

    return leader_url, followers
