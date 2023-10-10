#!/usr/bin/env python3
import rospy

# Behaviour Tree Packages
from ros_trees.trees import BehaviourTree
from ros_trees.leaves_common.console import Print
from py_trees.composites import Sequence, Selector
from py_trees.decorators import FailureIsRunning, SuccessIsRunning, OneShot

# Package Specific Leaves and Branches
from custom_tree.leaves.general import Wait, GetUICommand
from custom_tree.branches.general import ExampleSequence

if __name__ == '__main__':
    # Create ROS node 
    rospy.init_node('example_behaviour_agent')

    # ----------- Initialise The Main Tree --------------------------------------------
    tree = BehaviourTree('Example Behaviour Agent Tree', 
        Selector(children=[
            # ----------- Example of Multiple Sequences ---------------------------#
            Sequence(children=[
                GetUICommand(value=1),
                Print(load_value="Running Sequence 1..."),
                Wait(duration=1),
                Print(load_value="Waited 1 second -> Completed Sequence 1!"),
            ]),
            Sequence(children=[
                GetUICommand(value=2),
                Print(load_value="Running Sequence 2..."),
                ExampleSequence(duration=2),
                Print(load_value="Completed Sequence 2!"),
            ]),
            # ----------- Runs a OneShot (on agent start) --------------- #
            # NOTE: only runs once as the name implies. Good for setting up your agent's intial functions
            #       e.g., move to a home pose, etc.
            OneShot(Sequence(children=[
                Print(load_value="Ran One Shot!"),
            ])),
        ])
    )

    # Run the selected Tree
    tree.run(
        hz=30, 
        push_to_start=False, 
        setup_timeout=5, 
        log_level='INFO'
    )

    # Comment out the run method above to visualise the tree (PDF, PNG)
    # tree.visualise()