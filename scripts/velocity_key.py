#!/usr/bin/env python
# license removed for brevity
import rospy
import roslib
import cv2
from geometry_msgs.msg import Twist

def talker(key):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    r = rospy.Rate(1) # 10hz

    str = Twist()
    str.linear.x = 0.0
    str.linear.y = 0.0
    str.linear.z = 0.0
    
    str.angular.x = 0.0
    str.angular.y = 0.0
    str.angular.z = 0.0
    
    if key == 119:
        str.linear.x = 2.0
    elif key == 115:
        str.linear.x = -2.0
    elif key == 97:
        str.angular.z = 2.0
    elif key == 100:
        str.angular.z = -2.0
    
    rospy.loginfo(str)
    pub.publish(str)
    r.sleep()

if __name__ == '__main__':
  rospy.init_node('velocity_key_c')
  image = cv2.imread(roslib.packages.get_pkg_dir('behinner_tutorials') + '/files/InputKey.png')
  cv2.imshow('InputWindow',image)
  r = rospy.Rate(10)
  while not rospy.is_shutdown():
    key = cv2.waitKey(1)

    rospy.loginfo(key)
    r.sleep()
    talker(key)
