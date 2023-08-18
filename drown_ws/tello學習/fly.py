from djitellopy import tello
from time import sleep

mytello = tello.Tello()
print('123',mytello)
print("id", id(mytello))
print(type(mytello))
b = mytello
b.connect()
#mytello.connect() #連線
print(mytello.get_battery())
#mytello.takeoff() #起飛
# mytello.send_rc_control(前/後, 左/右, 上/下, 速度)
# 裡面的4個數質都是100~ -100之間可自由調整
#mytello.send_rc_control(0, 0, 50, 0) #向上
#sleep(2)
#mytello.send_rc_control(0, 0, 0, 0) #全部停止
#mytello.land() #著陸
