#!/usr/bin/env python3
"""
Python module containing 'generic' leaves 

Generic in this context, are useful additional leaves (i.e., printing info)
"""

# ADD General imports HERE
import rospy
import os

# ROS TREES Imports (add more or less as needed)
from ros_trees.leaves import Leaf
from ros_trees.leaves_ros import ActionLeaf, SubscriberLeaf, ServiceLeaf, PublisherLeaf

# ADD ROS message imports HERE
from std_msgs.msg import Int32

# ADD Project specific imports HERE

# Update Path Variable to main package
__path__ = os.path.realpath(os.path.join(os.path.dirname(__file__), '../../..'))

### -------------------------------- Leafs ----------------------------------- ###
class Wait(Leaf):
    """
    General Wait Leaf (Waits in Seconds)
    """
    def __init__(self, name='Wait', duration=1):
        super().__init__(
            name=name,
            load_fn=self.load_fn,
            eval_fn=self.eval_fn,
            save=False
        )
        self.duration = duration

    def load_fn(self):
        self.start = rospy.get_time()
        return None

    def eval_fn(self, value):
        return True

    def _is_leaf_done(self):
        return rospy.get_time() - self.start > self.duration

### --------------------------------  Subscriber Leafs ----------------------------------- ###
class GetUICommand(SubscriberLeaf):
    """
    This leaf will query if a UI command is available
    Publish to the defined topic_name the topic_class type and validate if found (see main tree example)
    """
    def __init__(self, 
        name="Get UI Start Command", 
        topic_name='/ui/control', 
        topic_class=Int32, 
        expiry_time=1, 
        timeout=0.1,
        value=None,
        *args, **kwargs):

        super().__init__(name=name, 
            topic_name=topic_name, 
            topic_class=topic_class, 
            expiry_time=expiry_time, 
            timeout=timeout, 
            eval_fn=self.eval_fn,
            *args, **kwargs)
        
        if value is None:
            raise Exception('Put a value in!!!')

        self.value = value

    def eval_fn(self, value):
        return value and value.data == self.value