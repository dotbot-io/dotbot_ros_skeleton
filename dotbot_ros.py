#!/usr/bin/env python


from rospy import Rate, Publisher, Subscriber, init_node
import rospy

class DotbotNode:
    main_rate = None
    node_name = 'dotbot_node'
    def __init__(self):
        init_node(self.node_name)
        self.setup()
        if self.main_rate is not None:
            while not rospy.is_shutdown():
                self.loop()
                self.main_rate.sleep()
        else:
            rospy.spin()

if __name__ == '__main__':
    try:
        from node import Node
        ne = Node()
    except rospy.ROSInterruptException:
        pass
