from dotbot_ros import DotbotNode
import dotbot_ros

class Node(DotbotNode):

    def setup(self):
        self.main_rate = dotbot_ros.Rate(1)
        print 'setup'

    def loop(self):
        print 'loop'
