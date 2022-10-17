#!/usr/bin/env python
"""OpenCV feature detectors with ros CompressedImage Topics in python.

This example subscribes to a ros topic containing sensor_msgs 
CompressedImage. It converts the CompressedImage into a numpy.ndarray, 
then detects and marks features in that image. It finally displays 
and publishes the new image - again as CompressedImage topic.
"""


# numpy and scipy
import numpy as np


# OpenCV
# Ros libraries
import rospy

# Ros Messages
from sensor_msgs.msg import CompressedImage , Image
# We do not use cv_bridge it does not support CompressedImage in python
# from cv_bridge import CvBridge, CvBridgeError


def callback(ros_data):
    pub=image_pub.publish(ros_data)

if __name__ == '__main__':
    image_pub = rospy.Publisher("/head_front_camera/color/image_raw",Image)
    subscriber = rospy.Subscriber("/head_front_camera/color/image_raw/compressed",CompressedImage, callback,  queue_size = 1)
    rospy.init_node('image_raw', anonymous=True)
    rospy.spin()


