
This project builds upon the functionalities provided by the [UAV_control API](https://github.com/Project-GrADyS/uav_control/tree/main) by implementing a practical example that uses its endpoints to control a fleet of drones. The leader drone follows a predefined route, and the followers maintain specific formations relative to the leader throughout the mission.

---

### How It Works

1. **Launching the System:**
   - Run the program with the following command:
     ```bash
     python3 main.py --n <number_of_drones> --formation <formation_name>
     ```
   - Example:
     ```bash
     python3 main.py --n 3 --formation triangle
     ```
     This launches one leader drone and two followers, arming them and taking off to positions based on the chosen formation.

2. **Leader Movement:**
   - The leader follows the route specified in the `route` variable in `main.py`.
   - The route consists of waypoints with GPS coordinates and altitude.

3. **Follower Movement:**
   - Followers adjust their positions dynamically to stay in formation as the leader moves.

4. **Formations:**
   - The formations define the relative positions of drones during the mission.
   - Available formations include:
     - `circle`
     - `triangle`
     - `square`
     - `pentagon`, `hexagon`, ... up to `decagon`
     - `cross`

---

### Prerequisites

1. **Python Version:**
   - Make sure Python 3.10 is installed.
2. **Dependencies:**
   - Install the required libraries using the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```
3. **`uav_control` API:**
   - This project relies on `uav_control` for drone simulation and control. It is automatically installed with the dependencies.

---

### Project Files Overview

| File Path                               | Description                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------|
| `protocol_testing.py`                   | Initializes the UAVs, setting up leader and follower configurations.       |
| `requirements.txt`                      | Contains the required dependencies.                                        |
| `main.py`                               | Main script that coordinates the entire mission.                           |
| `clean.sh`                              | Terminates all running drone simulations and related processes.            |
| `utils/api.py`                          | Contains functions for drone actions such as arming, takeoff, and location retrieval. |
| `utils/auxiliar.py`                     | Provides utility functions for GPS conversions and distance calculations.  |
| `utils/formations.py`                   | Defines drone formations like circle, triangle, and cross.                 |
| `leader_control/leader.py`              | Handles movement commands for the leader drone.                            |
| `follower_control/follower.py`          | Handles movement commands for the follower drones.                         |

---

### How to Clean Up

Run the `clean.sh` script to stop any running simulations or processes:

```bash
bash clean.sh
