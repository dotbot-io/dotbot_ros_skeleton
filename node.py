from dotbot_ros import DotbotNode
import dotbot_ros

class Node(DotbotNode):
    main_rate = dotbot_ros.Rate(1)

    
