import rospy
import cv2, time
from std_msgs.msg import String, Float32MultiArray,Int32MultiArray,Bool
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np
import os

def callback(data):
    img = np.array(data.data,dtype=np.uint8).reshape(240,360,3)
    #img = cv2.resize(data.data, (360, 240))
    print(img)
    cv2.imshow("Mytello2", img)
    cv2.waitKey(1)
def over(data):
    ov = data.data
    if ov:
        cv2.destroyAllWindows()
        os._exit(0)
def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('frame_img', Int32MultiArray, callback)
    rospy.Subscriber('over',Bool,over)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
