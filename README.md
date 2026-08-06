# ROS2 Turtle Task

## Overview
This project demonstrates basic ROS2 communication using Publisher and Subscriber nodes, along with controlling the TurtleSim robot to move in a square path.

## Features
- Publisher Node
- Subscriber Node
- TurtleSim square movement
- Python implementation using ROS2

## Project Structure

```
ros_turtle_task/
├── my_robot/
│   ├── publisher.py
│   ├── subscriber.py
│   ├── turtle_square.py
│   └── __init__.py
├── package.xml
├── setup.py
├── setup.cfg
├── resource/
└── test/
```

## Requirements

- Ubuntu 24.04
- ROS2 Jazzy
- Python 3

## Build

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

## Run Publisher

```bash
ros2 run my_robot publisher
```

## Run Subscriber

```bash
ros2 run my_robot subscriber
```

## Run Turtle Square

```bash
ros2 run my_robot turtle_square
```

## Author

**Adel Ateeq**
