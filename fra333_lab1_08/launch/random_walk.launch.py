#!usr/bin/python3
import turtle
from launch import LaunchDescription
from launch.actions import ExecuteProcess,DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
def generate_launch_description():

    rate = LaunchConfiguration('rate')
    rate_launch_arg = DeclareLaunchArgument('rate',default_value='5.0')
    # launch_description.add_action(rate_launch_arg)
    
    ### Example for adding a node ###
    
    turtle1 = Node(
        package='turtlesim',
        executable='turtlesim_node',
        parameters=[
            {'background_b':100},
            {'background_b':20},
            {'background_b':100},
        ]
    )

    linear = Node(
        package='fra333_lab1_08',
        executable='noise_generator.py',
        namespace= 'linear',
        arguments= [rate],
        remappings=[
            ('/noise','/linear/noise')
        ]
    )

    angular = Node(
        package='fra333_lab1_08',
        executable='noise_generator.py',
        namespace= 'angular',
        arguments=[rate],
        remappings=[
            ('/noise','/angular/noise')
        ]
    )

    velocity = Node(
        package='fra333_lab1_08',
        executable='velocity_mux.py',
        arguments=[rate],
    )

    mux = [rate_launch_arg,turtle1,linear,angular,velocity]
    return LaunchDescription(mux)

    