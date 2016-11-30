#!/usr/bin/env python

from rospy import Rate, Subscriber, init_node
import rospy

def Publisher(name, msg_type, queue_size=50):
    return rospy.Publisher(name, msg_type, queue_size=queue_size)

class DotbotNode:
    loop_rate = None
    node_name = 'node'
    def __init__(self):
        init_node(self.node_name)
        self.setup()
        if self.loop_rate is not None:
            while not rospy.is_shutdown():
                self.loop()
                self.loop_rate.sleep()
        else:
            rospy.spin()

if __name__ == '__main__':
    try:
        from node import Node
        ne = Node()
    except rospy.ROSInterruptException:
        pass
