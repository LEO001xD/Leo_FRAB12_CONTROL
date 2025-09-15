from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Keyboard Control Node
        Node(
            package='keyboard_control',
            executable='keyboard_node',
            name='keyboard_control',
            output='screen'
        ),

        # Microcontroller Bridge Node >> yung mai me
        Node(
            package='microcontroller_bridge',
            executable='bridge_node',
            name='microcontroller_bridge',
            output='screen'
        ),

        # Vision Node >> yung mai me
        Node(
            package='vision_node',
            executable='vision_node',
            name='vision_node',
            output='screen'
        ),
    ])

