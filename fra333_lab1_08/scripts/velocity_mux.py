#!/usr/bin/python3
# import all other neccesary libraries

import cmd
from cmd import Cmd
from operator import imod
from std_msgs.msg import Float64
import sys

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class VelocityMux(Node):
    def __init__(self):
        if len(sys.argv) >= 2: 
            self.rate = float(sys.argv[1])

        else:
            self.rate = 5.0 #Hz
        
        # add codes here
        super().__init__('Node')
        self.publisher = self.create_publisher(Twist , '/turtle1/cmd_vel' ,10 ) #Topic : cmd_vel
        timer_period = 1/ self.rate
        self.timer = self.create_timer ( timer_period ,self.timer_callback )
        self.subscription1 = self.create_subscription (Float64 , '/linear/noise' , self.linear_vel_sub_callback , 10)
        self.subscription2 = self.create_subscription (Float64 , '/angular/noise' , self.angular_vel_sub_callback , 10)
        self.cmd_vel = Twist()


    def linear_vel_sub_callback(self,msg:Float64):
        # remove pass and add codes here
        self.cmd_vel.linear.x = msg.data
        self.get_logger().info("linear: {0}".format(self.cmd_vel.linear.x))
        
    
    def angular_vel_sub_callback(self,msg:Float64):
        # remove pass and add codes here
        self.cmd_vel.angular.z = msg.data
        self.get_logger().info("angular: {0}".format( self.cmd_vel.angular.z))
    
    def timer_callback(self):
        # remove pass and add codes here
        self.publisher.publish(self.cmd_vel) 

def main(args=None):
    # remove pass and add codes here
        rclpy.init(args=args)
        velocity = VelocityMux()
        rclpy.spin(velocity)
        velocity.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    main()