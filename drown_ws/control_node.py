import keyboardModule as kb
from djitellopy import tello
from time import sleep
import cv2, time
import rospy
import sys,os
from std_msgs.msg import String,Float32MultiArray, Int32MultiArray,Bool
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

"""
    if kb.getKey("q"):
        mytello.land()
    elif kb.getKey("z"):
        mytello.takeoff()
"""
#mytello = tello.Tello()
#mytello.connect()
#print('123',mytello)
#print(type(mytello))
#print("目前電池電量: {}%".format(mytello.get_battery()))
#camera = False
#mytello.streamoff()
#kb.init()
pub_img = rospy.Publisher('frame_img', Int32MultiArray,queue_size=10)
def callback(data):
    val =data.data
    print(data.data)
    if val[4]==1:
        mytello.takeoff()
    if val[5]==1:
        mytello.land()
    #rospy.loginfo(rospy.get_caller_id() + ' I heard %s', data.data)
    lr, fb, ud, yv = int(val[0]), int(val[1]), int(val[2]), int(val[3])
    mytello.send_rc_control(lr, fb, ud, yv)

def camera(data):
    val = data.data
    print(data.data)
    if val[0]:
        if not mytello.stream_on:
            #mytello.streamoff()
            mytello.streamon()
            img = mytello.get_frame_read().frame
            img = cv2.resize(img, (360, 240))
            cv2.imshow("Mytello", img)
            cv2.waitKey(1)
            a = Int32MultiArray(data = img.reshape(-1).tolist())
            pub_img.publish(a)
            sleep(0.05)
        else:
            mytello.streamoff()
            cv2.destroyAllWindows()
    if not val[0]:
        if mytello.stream_on:
            img = mytello.get_frame_read().frame
            img = cv2.resize(img, (360, 240))
            cv2.imshow("Mytello", img)
            cv2.waitKey(1)
            a = Int32MultiArray(data = img.reshape(-1).tolist())
            pub_img.publish(a)
            sleep(0.05)
    if val[1] and mytello.stream_on:
        cv2.imwrite(r"saveImg/{}.jpg".format(time.time()), img)
        sleep(0.5)
def over(data):
    ov = data.data
    print(data.data)
    if ov:
        print("omg")
        if mytello.stream_on:
            mytello.streamoff()
        if mytello.is_flying:
            mytello.land()
        #os._exit(0)
def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    #rate = rospy.Rate(10)
    #timer = rospy.Timer(rospy.Duration(1),frame_callback)
    #rospy.spin()
    #timer.shutdown()
    #while not rospy.is_shutdown():
    rospy.Subscriber('over',Bool,over)
    rospy.Subscriber('move', Float32MultiArray, callback)
    rospy.Subscriber('camera',Int32MultiArray,camera)
    img = mytello.get_frame_read().frame
    img = cv2.resize(img,(360,240))
    rospy.spin()
        #rate.sleep()

if __name__ == '__main__':
    mytello = tello.Tello()
    mytello.connect()
    print("目前電池電量: {}%".format(mytello.get_battery()))
    listener()
    
