from djitellopy import tello
from time import sleep
import cv2, time

mytello = tello.Tello()
mytello.connect(True)
print("目前電池電量: {}%".format(mytello.get_battery()))

# Command 'takeoff' was unsuccessful for 4 tries. Latest response:'error' :沒電了

mytello.takeoff()
sleep(1)
mytello.land()
if not mytello.stream_on:
    #pass
    #mytello.streamoff()
    mytello.streamoff()

while True:
    img = mytello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Mytello", img)
    key = cv2.waitKey(1)
    sleep(0.05)
    if key==ord('q') or key==27:
        break

mytello.go_xyz_speed(50,0,0,10) # 查看 Tello SDK 文檔，您可以要求它移動的最小距離是 20 厘米：
sleep(0.05)
mytello.go_xyz_speed(-50,0,0,10)
mytello.streamoff()
mytello.land()
