#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from time import sleep

v=2       #reference linear velocity
w=1.25    #reference angular velocity

def move(v):
	pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
	rospy.init_node('my_initials',anonymous=True)
	vel=Twist()
	vel.linear.x=v
	vel.linear.y=vel.linear.z=0
	vel.angular.x=vel.angular.y=vel.angular.z=0
	
	t0=rospy.Time.now().to_sec()
	while not rospy.is_shutdown():
		pub.publish(vel)
		if rospy.Time.now().to_sec()>1+t0:
			break 

	vel.linear.x=0
	pub.publish(vel)

def rotate(w):
	pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
	rospy.init_node('my_initials',anonymous=True)
	vel=Twist()
	vel.linear.x=vel.linear.y=vel.linear.z=0
	vel.angular.x=vel.angular.y=0
	vel.angular.z=w
    
	t0=rospy.Time.now().to_sec()
	while not rospy.is_shutdown():
		pub.publish(vel)
		if rospy.Time.now().to_sec()>1+t0:
		   	break 

	vel.angular.z=0
	pub.publish(vel)

def write_initial():
	pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
	rospy.init_node('my_initials',anonymous=True)
	vel=Twist()
	vel.linear.x=vel.linear.y=vel.linear.z=0
	vel.angular.x=vel.angular.y=vel.angular.z=0
	pub.publish(vel)
	sleep(1)
	rotate(w)
	move(2*v)
	rotate(-2*w)
	move(2*v)
	move(-0.8*v)
	rotate(w)
	move(-0.8*v)

if __name__=="__main__":
	write_initial()

