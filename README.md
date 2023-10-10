<!-- Created with QCR's code template tool: https://github.com/qcr/code_templates -->

# example_behaviour_agent

[![QUT Centre for Robotics Open Source](https://github.com/qcr/qcr.github.io/raw/master/misc/badge.svg)](https://qcr.github.io)

<!--
Replace REPO_USER, & REPO_NAME in the lines below to get more auto-generated badges
![Primary language](https://img.shields.io/github/languages/top/REPO_USER/REPO_NAME)
[![License](https://img.shields.io/github/license/REPO_USER/REPO_NAME)](./BSD.txt)
-->

example_behaviour_agent is a basic implementation to get anyone started using behaviour trees (py trees).

The following packages are required (see install below). You can visit this to get more information:
- [ros_trees](https://github.com/qcr/ros_trees)

The following packages allow for some extra materials to assit with understanding the process (on top of ros_trees)
- [ros_trees_qcr](https://github.com/qcr/ros_trees_qcr): These are QCR specific leaves/branches that may be of use in your application
- [ros_trees_examples](https://github.com/qcr/ros_trees_examples): These are examples that can assist with the process

## Installation

example_behaviour_agent can be installed with the following commands:
```bash
# Clone package to a ROS workspace
cd ~/catkin_ws/src
git clone git@github.com:qcr/example_behaviour_agent.git

# Clone in the ros_trees ROS package (NEEDED)
git clone https://github.com/qcr/ros_trees.git

# Clone in some additional helper packages (examples, etc.)
git clone https://github.com/qcr/ros_trees_examples.git
git clone https://github.com/qcr/ros_trees_qcr.git

# Move to workspace root and run the following to build
cd ~/catkin_ws
rosdep install --from-paths src --ignore-src -r -y
catkin_make

# Source workspace to run
source ~/catkin_ws/devel/setup.bash
``` 

## Usage

example_behaviour_agent is used with the following commands:
```bash
# Run the example behaviour agent with the following command:
rosrun example_behaviour_agent example_agent.py
```