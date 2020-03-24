#!/usr/bin/env python
# license removed for brevity
import rospy
# from std_msgs.msg import String
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz
    # num = 0
    while not rospy.is_shutdown():
        
        # num = num + 1
        # str = String()
        # str.data = "hello world"
        str = Twist()
        str.linear.x = 2.0
        str.linear.y = 0.0
        str.linear.z = 0.0
        
        str.angular.x = 0.0
        str.angular.y = 0.0
        str.angular.z = 0.0
        
        # str.linear 
        
        rospy.loginfo(str)
        pub.publish(str)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
