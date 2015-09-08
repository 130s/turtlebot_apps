#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

/**
 * This tutorial demonstrates simple sending of geometry_msgs/Twist messages to Turtlebot over the ROS system. Originally explained in http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29
 */
int main(int argc, char **argv)
{
  ros::init(argc, argv, "sample_cmd_vel_sender");
  ros::NodeHandle n;
  ros::Publisher sample_cmdvel_pub = n.advertise<geometry_msgs::Twist>("/mobile_base/commands/velocity", 1000);

  geometry_msgs::Twist msg;
  ros::Rate loop_rate(5);
  int count = 0;
  while (ros::ok())
  {
    msg.linear.x = 0.3;
    msg.angular.z = 1.57;
    ROS_INFO("count%d msg.linear.x= %6.4lf", count, msg.linear.x);
    sample_cmdvel_pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
    ++count;
  }
  return 0;
}
