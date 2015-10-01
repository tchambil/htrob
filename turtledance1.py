#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
class square:
    """ This example is in the form of a class. """

    def __init__(self):
        rospy.on_shutdown(self.cleanup)
      	self.pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist)
        rospy.sleep(1)
        r = rospy.Rate(10.0)

        while not rospy.is_shutdown():
            # create a Twist message, fill it in to drive forward
            twist = Twist()
            twist.linear.x = -1.15*0.83*4
            for i in range(10):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()
                print twist.linear.x
 		
            twist = Twist()
            twist.linear.x = 0.15*0.83*4     
            for i in range(10):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()
                print twist.linear.x

        """   twist = Twist()
            twist.angular.z = 1.57/2*0.3     
            for i in range(10):         # 10*5hz = 2sec
                self.pub.publish(twist)
                r.sleep()
                print twist.angular.z
            
        """
    def cleanup(self):
        # stop the robot!
        twist = Twist()
        self.pub.publish(twist)

if __name__=="__main__":
    rospy.init_node('square')
    square()
