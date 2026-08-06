import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class TurtleSquare(Node):

    def __init__(self):
        super().__init__('turtle_square')

        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        time.sleep(1)

        self.move_square()

    def move_square(self):
        msg = Twist()

        for i in range(4):

            # Move Forward
            msg.linear.x = 2.0
            msg.angular.z = 0.0

            self.publisher.publish(msg)
            time.sleep(2)

            # Stop
            msg.linear.x = 0.0
            self.publisher.publish(msg)
            time.sleep(0.5)

            # Turn 90 degrees
            msg.angular.z = 1.57
            self.publisher.publish(msg)
            time.sleep(1)

            # Stop
            msg.angular.z = 0.0
            self.publisher.publish(msg)
            time.sleep(0.5)

        self.get_logger().info("Square Completed")


def main(args=None):
    rclpy.init(args=args)

    node = TurtleSquare()

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
