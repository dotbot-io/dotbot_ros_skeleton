from dotbot_ros import DotbotNode
import dotbot_ros

class Node(DotbotNode):
    main_rate = dotbot_ros.Rate(1)

    def setup(self):
        print 'setup'

    def loop(self):
        print 'loop'
