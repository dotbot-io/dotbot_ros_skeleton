#!/usr/bin/env python


from rospy import Rate, Publisher, Subscriber

class DotbotNode:
    main_rate = None

    def __init__(self):
        self.setup()
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
