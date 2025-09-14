import sys
import termios
import tty
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class KeyboardControl(Node):
    def __init__(self):
        super().__init__('keyboard_control')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info("Keyboard control started. Use WASD to move, Q to quit.")

    def run(self):
        settings = termios.tcgetattr(sys.stdin)
        try:
            while rclpy.ok():
                key = self.get_key(settings)
                twist = Twist()
                if key == 'w':
                    twist.linear.x = 0.5
                elif key == 's':
                    twist.linear.x = -0.5
                elif key == 'a':
                    twist.angular.z = 0.5
                elif key == 'd':
                    twist.angular.z = -0.5
                elif key == 'q':
                    break
                self.publisher_.publish(twist)
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

    def get_key(self, settings):
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardControl()
    node.run()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

