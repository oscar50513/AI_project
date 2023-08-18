#!/usr/bin/env python
# license removed for brevity
import keyboardModule as kb
from time import sleep
import cv2, time
import rospy
from std_msgs.msg import String, Float32MultiArray, Int32MultiArray,Bool
from djitellopy import tello
import sys
import pygame
kb.init()
def getKeyboardInput():
    lr, fb, ud, yv, up, down = 0, 0, 0, 0, 0, 0
    speed = 30
    if kb.getKey("z"):
        up = 1
    elif kb.getKey("q"):
        down = 1
    if kb.getKey("LEFT"):
        print(kb.getKey("LEFT"))
        lr = -speed
    elif kb.getKey("RIGHT"):
        print(kb.getKey("RIGHT"))
        lr = speed

    if kb.getKey("UP"):
        print(kb.getKey("UP"))
        fb = speed
    elif kb.getKey("DOWN"):
        print(kb.getKey("DOWN"))
        fb = -speed

    if kb.getKey("w"):
        print(kb.getKey("w"))
        ud = speed
    elif kb.getKey("s"):
        print(kb.getKey("s"))
        ud = -speed

    if kb.getKey("a"):
        print(kb.getKey("a"))
        yv = -speed
    elif kb.getKey("d"):
        print(kb.getKey("d"))
        yv = speed

    return [lr, fb, ud, yv, up, down]

def camera():
    if kb.getKey('f'):
        print(kb.getKey('f'))
        return [1,0]
    if kb.getKey("p"):
        print(kb.getKey("p"))
        return [0,1]
    return [0,0]
    
def over():
    print('over')
    mykey = pygame.key.get_pressed()
    if mykey[pygame.K_ESCAPE]:
        print('esc')
        pygame.quit()
        return True
    return False
    
def talker():
    pub = rospy.Publisher('move',  Float32MultiArray, queue_size=10)
    pub_c = rospy.Publisher('camera',Int32MultiArray,queue_size=10)
    pub_o = rospy.Publisher('over',Bool,queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        val = getKeyboardInput()
        a = Float32MultiArray(data = val)
        rospy.loginfo(a)
        pub.publish(a)
        
        cam = camera()
        b = Int32MultiArray(data = cam)
        rospy.loginfo(b)
        pub_c.publish(b)
        if cam[0]==1:
            sleep(15)

        ov = over()
        rospy.loginfo(ov)
        pub_o.publish(ov)
        if ov:
            b = Int32MultiArray(data = [1,0])
            pub_c.publish(b)
            break

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
