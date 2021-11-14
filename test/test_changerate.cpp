#include "Fiesta.h"

int main(int argc, char **argv) {
  ros::init(argc, argv, "FIESTA");
  ros::NodeHandle node("~");
  fiesta::Fiesta<sensor_msgs::PointCloud2::ConstPtr, nav_msgs::Odometry::ConstPtr> esdf_map(node);
  ros::spin();
  return 0;
}
