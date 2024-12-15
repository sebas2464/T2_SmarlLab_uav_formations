## UAV Formation Control Project

This project enables the control of a drone fleet in a leader-follower architecture. The leader drone follows a predefined route, while the follower drones maintain a specific formation relative to the leader throughout the journey.

---

### How It Works

1. **Launching the System:**
   - Run the program using:
     ```bash
     python3 main.py --n <number_of_drones> --formation <formation_name>
     ```
   - Example:
     ```bash
     python3 main.py --n 3 --formation triangle
     ```
     This will:
     - Launch **1 leader drone** and **2 follower drones**.
     - The drones will arm and take off to initial positions defined by the selected formation (e.g., `triangle`).

2. **Leader Movement:**
   - The leader drone follows a predefined route specified in the `route` variable in `main.py`.
   - Each waypoint in the route includes GPS coordinates and altitude.

3. **Follower Movement:**
   - The follower drones maintain the selected formation while following the leader.
   - Their GPS positions are dynamically adjusted to stay in formation as the leader moves through the waypoints.

4. **Formations:**
   - Formations determine the relative positions of the drones at all times.
   - Supported formations include:
     - `circle`
     - `triangle`
     - `square`
     - `pentagon`, `hexagon`, ... up to `decagon`
     - `cross`

---

### Prerequisites

1. **Python Version**: Python 3.10 is required.
2. **Dependencies**:
   - Install all dependencies using the provided `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

3. **Install `uav_control`:**
   - This repository relies on `uav_control` for UAV control and simulation.
   - The `uav_control` repository will be automatically installed via `pip` as part of `requirements.txt`.

---

### Project Files Overview

| File Path                               | Description                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------|
| `protocol_testing.py`                   | Handles the initialization of UAVs, setting up leader and follower roles.  |
| `requirements.txt`                      | Lists project dependencies, including external libraries and repositories. |
| `main.py`                               | Main entry point for the project; orchestrates drone operations.           |
| `clean.sh`                              | Script to terminate running drone simulations and related processes.       |
| `utils/api.py`                          | Contains helper functions for drone commands such as arm, takeoff, etc.    |
| `utils/auxiliar.py`                     | Provides utilities for GPS coordinate transformations and distance calcs.  |
| `utils/formations.py`                   | Defines various drone formations (e.g., circle, square, cross).            |
| `leader_control/leader.py`              | Implements leader drone movement commands.                                 |
| `follower_control/follower.py`          | Implements follower drone movement commands.                               |

---

### About `uav_control`

`uav_control` is an external API used for UAV autonomous flights. It supports both simulated and real-world drone control. The repository is automatically installed when you install the project requirements.

---

### How to Clean Up

Use the `clean.sh` script to terminate all UAV-related processes:

```bash
bash clean.sh
