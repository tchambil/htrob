#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math

dist_to_start = 0
current_angle = 0
max_dist = 1.0
x_velocity = 0.2
angular_velocity = -0.4

def reciver_odom(data):
    global current_angle
    global dist_to_start
    rospy.loginfo
    pose=data.pose.pose
    quaternion = (pose.orientation.x,pose.orientation.y,pose.orientation.z,pose.orientation.w)
    (roll , pitch , yaw) = euler_from_quaternion(quaternion)
    tAngle = math.degrees(yaw)
    if (tAngle<0):
       tAngle = tAngle+360
    current_angle = tAngle
    dist_to_start = math.sqrt(pow(data.pose.pose.position.x,2)+pow(data.pose.pose.position.y,2)) #calculo de la distancia con x2 e y2 = 0
#Paso 4
def go_back(twist,pub,r,direction):
    global dist_to_start
    twist.linear.x = direction*x_velocity
    twist.linear.y=0.0
    twist.linear.z=0.0
    twist.angular.z = 0.0 
    while abs(dist_to_start - max_dist) > 0.2:
        print "retrocediendo ..."
        print "distancia al inicio:",dist_to_start
        print "diff al inicio y actual:",abs(dist_to_start - max_dist)
        pub.publish(twist)
        r.sleep()
    rospy.sleep(1)
#Paso 3
def go(twist,pub,r,direction):
    global dist_to_start
    twist = Twist()
    twist.linear.x = direction*x_velocity
    twist.linear.y=0.0
    twist.linear.z=0.0
    twist.angular.z = 0.0 
    while abs(dist_to_start - max_dist) <0.8:
        print "Avanzando . . ."
        print "distancia al inicio:",dist_to_start
        print "diff al inicio y actual:",abs(dist_to_start - max_dist)
        pub.publish(twist)
        r.sleep()
    rospy.sleep(1)
#Paso 1,2,4,5
def spin(twist,pub,r,max_angle,diff = 0):
    global current_angle
    twist = Twist()
    twist.angular.z = angular_velocity
    twist
    if max_angle == 360:
        print "360"
        while current_angle > 3.0:
            print "angulo actual _360:",current_angle
            print "diff angulo actual y max angle:",abs(current_angle - max_angle) 
            pub.publish(twist)
            r.sleep()
    else:
        max_angle = 360 - max_angle
        while abs(max_angle - current_angle) > diff:
            print "angulo actual_90:",current_angle
            print "diff angulo actual y max angle:",abs(current_angle - max_angle) 
            pub.publish(twist)
            r.sleep()
    rospy.sleep(4)

def dance():
    rospy.init_node('moonwalk')
    pub = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=10)
    rospy.Subscriber('odom',Odometry, reciver_odom)  
    rate = rospy.Rate(10) # 10hz
    twist = Twist()
    rospy.sleep(1)
    i = 1
    while not rospy.is_shutdown():
        print "Numero repeticion:",i
        spin(twist,pub,rate,360) #giro 360
        spin(twist,pub,rate,90,3) #giro 90
        if i%2 == 0:
            go(twist,pub,rate,1)
        else:
            go_back(twist,pub,rate,-1)
        i+=1
if __name__ == '__main__':
    try:
        dance()
    except rospy.ROSInterruptException:
        pass
