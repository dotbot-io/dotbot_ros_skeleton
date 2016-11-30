#!/usr/bin/env python


from rospy import Rate, Publisher, Subscriber, init_node

class DotbotNode:
    main_rate = None
    node_name = 'dotbot_node'
    def __init__(self):
        self.setup()
        init_node(self.node_name)
        if self.main_rate is not None:
            while not rospy.is_shutdown():
                self.loop()
                self.main_rate.sleep()
        else:
            rospy.spin()

if __name__ == '__main__':
    import rospy
    try:
        from node import Node
        ne = Node()
    except rospy.ROSInterruptException:
        pass
