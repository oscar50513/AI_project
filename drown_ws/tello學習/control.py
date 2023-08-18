import keyboardModule as kb
from djitellopy import tello
from time import sleep
import cv2, time

mytello = tello.Tello()
mytello.connect(False)
print('123',mytello)
print(type(mytello))
# print("目前電池電量: {}%".format(mytello.get_battery()))
mytello.streamon()
kb.init()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 40
    if kb.getKey("q"):
        mytello.land()
    elif kb.getKey("z"):
        mytello.takeoff()

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

    if kb.getKey("p"):
        cv2.imwrite(r"saveImg/{}.jpg".format(time.time()), img)
        sleep(0.5)
    return [lr, fb, ud, yv]

while True:
    val = getKeyboardInput()
    print(val)
    lr, fb, ud, yv = val[0], val[1], val[2], val[3]
    mytello.send_rc_control(lr, fb, ud, yv)
    # img = mytello.get_frame_read().frame
    # img = cv2.resize(img, (360, 240))
    # cv2.imshow("Mytello", img)
    # cv2.waitKey(1)
    sleep(0.05)
