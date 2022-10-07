#!/usr/bin/python3

# import all other neccesary libraries here

import sys

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from lab1_interfaces.srv import SetNoise
import numpy as np
from math import sqrt

class NoiseGenerator(Node):

    def __init__(self):
        # get the rate from argument or default
        if len(sys.argv) >= 2: 
            self.rate = float(sys.argv[1])

        else:
            self.rate = 5.0 #Hz

        # add codes here
        super().__init__('set_noise')
        self.publisher = self.create_publisher(Float64,'/noise',10)
        self.srv = self.create_service(SetNoise, 'set_noise', self.set_noise_callback)

        timer_period = 1/self.rate #second
        self.timer = self.create_timer(timer_period,self.timer_callback)

        # additional attributes
        self.mean = 0.0
        self.variance = 1.0
        self.get_logger().info(f'Starting {self.get_namespace()}/{self.get_name()} with the default parameter. mean: {self.mean}, variance: {self.variance}')
    
    def set_noise_callback(self,request:SetNoise.Request,response:SetNoise.Response):
        # add codes here
        self.mean = request.mean.data
        self.variance = request.variance.data
        return response
    
    def timer_callback(self):
        # remove pass and add codes here
        msg = Float64()
        msg.data = np.random.normal(self.mean,sqrt((self.variance)),None)
        self.publisher.publish(msg)
        self.get_logger().info('mean: %d,variance: %d' % (self.mean,self.variance))
        # pass

def main(args=None):
    # remove pass and add codes here
    rclpy.init(args=args)
    noise_generator = NoiseGenerator()
    print("Hello")
    rclpy.spin(noise_generator)
    noise_generator.destroy_node()
    rclpy.shutdown()
    # pass

if __name__=='__main__':
    main()