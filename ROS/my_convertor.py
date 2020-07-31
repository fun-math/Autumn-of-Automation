#!/usr/bin/env python

import rospy
from math import atan2,asin,pi
from time import sleep
from my_package.msg import quaternions
from my_package.msg import euler_angles

def talker(my_output):
	pub = rospy.Publisher('topic2',euler_angles,queue_size=10)
	rospy.init_node('my_converter',anonymous=True)
	sleep(1)

	if not rospy.is_shutdown():
		pub.publish(my_output)

def callback(my_input):
	output=euler_angles()
	w=my_input.w
	x=my_input.x
	y=my_input.y
	z=my_input.z
	output.roll=atan2((2*(w*x+y*z)),1-2*(x*x+y*y))
	if -1<2*(w*x-y*z)<1:
		output.pitch=asin(2*(w*x-y*z))
	else :
		output.pitch=pi/2		
	output.yaw=atan2(2*(w*z+x*y),1-2*(y*y+z*z))
	talker(output)

def listener():
	rospy.init_node('my_converter',anonymous=True)

	rospy.Subscriber('topic1',quaternions,callback)

	rospy.spin()

if __name__=='__main__':
	listener()
