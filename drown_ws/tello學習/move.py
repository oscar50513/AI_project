from djitellopy import tello
from time import sleep

def connAndbatttery():
    global mytello
    mytello = tello.Tello()
    mytello.connect() #連線
    print(mytello.get_battery())

def takeoff():
    mytello.takeoff() #起飛
    mytello.send_rc_control(0, 0, 50, 0) #向上
    sleep(3)
    mytello.send_rc_control(0, 0, 0, 0) #全部停止
    mytello.land() #著陸

def forwardAndBack():
    mytello.takeoff()
    mytello.send_rc_control(0, 0, 50, 0)  # 向上
    sleep(3)
    mytello.send_rc_control(0, 50, 0, 0)  # 向左
    sleep(2)
    mytello.send_rc_control(0, -50, 0, 0)
    mytello.send_rc_control(0, 0, 0, 0)
    sleep(2)
    mytello.land()
def leftAandRight():
    mytello.takeoff()
    mytello.send_rc_control(0, 0, 50, 0)  # 向上
    sleep(3)
    mytello.send_rc_control(50, 0, 0, 0)
    sleep(2)
    mytello.send_rc_control(-50, 0, 0, 0)
    mytello.send_rc_control(0, 0, 0, 0)
    sleep(2)
    mytello.send_rc_control(0, 0, 0, 0)
    sleep(2)
    mytello.land()
connAndbatttery()
#takeoff()
#forwardAndBack()
leftAandRight()
takeoff()
