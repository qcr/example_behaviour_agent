#!/usr/bin/env python3

# Behaviour Tree Packages (Sequences, Selectors, Decorators, etc)
# See https://py-trees.readthedocs.io/en/devel/ for more information
# NOTE: ros_trees is behind a couple of versions, so some leaves may be out of date
from py_trees.composites import Sequence, Selector
from py_trees.decorators import FailureIsRunning, SuccessIsFailure
from ros_trees.leaves_common.console import Print

# ADD robot/project specific Leaves/Branches/ROS messages HERE
from custom_tree.leaves.general import Wait

# ------------------------------ High Level Movement Sequences ------------------------------------
class ExampleSequence(Sequence):
    """
    Describes a sequence of behaviours as an example
    NOTE: define inputs to the class initialisation method (see duration example)
    """
    def __init__(self, 
            name="Example Sequence",
            duration=2,
            *args, **kwargs):
        super().__init__(name, [
            # Example of a console print for debugging purposes
            Print(load_value="Running a Test Behaviour Sequence..."),
            # Example of a leaf being used in sequence (Wait). Note the param input for duration
            Wait(duration=duration),
            Print(load_value="Waited for {} seconds".format(duration)),
        ])
