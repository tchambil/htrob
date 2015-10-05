#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist

 #vuelta completa Paso 1
def girar_180(pub,r):
    twist = Twist()
    twist.angular.z = 1.57   # 180 degrees
    for i in range(20):         # 10*5hz = 2sec
        pub.publish(twist)
        r.sleep()
    rospy.sleep(1)

#girar 90 paso 2
def girar_90(pub,r):
    twist = Twist()
    twist.angular.z = 1.57/2   # 90 degrees
    for i in range(10):         # 10*5hz = 2sec
        pub.publish(twist)
        r.sleep()
    rospy.sleep(1)

#avanza hacia atras paso 3
def avanza(pub,r):
    twist2 = Twist()
    twist2.linear.x = 0.5
    twist = Twist()
    twist.linear.x = -0.5  
    for i in range(40):         # 10*5hz = 2
        pub.publish(twist)
        rospy.Rate(10).sleep()
    rospy.sleep(1)   
 #vuelta 180 paso 4
def girar_1802(pub,r):
    twist = Twist()
    twist.angular.z = 1.57   # 180 degrees por segundo
    for i in range(10):         # 10*5hz = 2sec
        pub.publish(twist)
        r.sleep()
    rospy.sleep(1)

 #avanza hacia atras 
def avanza_atraz(pub,r):
    twist = Twist()
    twist.linear.x = -0.5  
    for i in range(40):         # 10*5hz = 2
        pub.publish(twist)
        rospy.Rate(10).sleep()
        print twist.linear.x
    rospy.sleep(1)

#vuelve a posicion original
def vuele_orginal(pub,r):
    twist = Twist()
    twist.angular.z = 1.57/2   # 90 degrees
    for i in range(10):         # 10*5hz = 2sec
        pub.publish(twist)
        r.sleep()
    rospy.sleep(2)

def main():
    pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist)
    rospy.sleep(1)
    r = rospy.Rate(5.0)
        
    while not rospy.is_shutdown():
        #vuelta completa Paso 1
        girar_180(pub,r)
        girar_90(pub,r)
        avanza(pub,r)
        girar_1802(pub,r)
        avanza_atraz(pub,r)
        vuele_orginal(pub,r)

if __name__ == '__main__':
    rospy.init_node('square')
    main()
