# ROS2 Turtle Task

## Overview
This project demonstrates basic ROS 2 communication using Publisher and Subscriber nodes, along with controlling the TurtleSim robot to move in a square path.

## Features

- Publisher Node
- Subscriber Node
- TurtleSim square movement
- Python implementation using ROS 2

## Project Structure

```text
ros_turtle_task/
├── my_robot/
│   ├── __init__.py
│   ├── publisher.py
│   ├── subscriber.py
│   └── turtle_square.py
├── resource/
├── test/
├── package.xml
├── setup.py
├── setup.cfg
└── README.md
```

## Requirements

- Ubuntu 24.04
- ROS 2 Jazzy
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
