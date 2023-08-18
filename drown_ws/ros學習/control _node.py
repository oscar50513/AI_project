import keyboardModule as kb
from djitellopy import tello
from time import sleep
import cv2, time
import rospy
from std_msgs.msg import String,Float32MultiArray

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

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
#print(data.data)
    global val
    val = data.data
    
    
    #lr, fb, ud, yv = val[0], val[1], val[2], val[3]
    #mytello.send_rc_control(lr, fb, ud, yv)

def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('move', Float32MultiArray, callback)
    rospy.spin()
"""
while True:
    val = getKeyboardInput()
    print(val)
    lr, fb, ud, yv = val[0], val[1], val[2], val[3]
    mytello.send_rc_control(lr, fb, ud, yv)
    img = mytello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Mytello", img)
    cv2.waitKey(1)
    listener()
    sleep(0.05)
"""
if __name__ == '__main__':
    global val
    listener()
    
