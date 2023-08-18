# 调用相关的模块
import socket
import threading
import time
import sys

# Tello的IP和接口
#tello_address = ('172.20.10.8', 8889)
tello_address = ('192.168.10.1', 8889)

# 本地电脑的IP和接口
local_address = ('', 9000)

# 创建一个接收用户指令的UDP连接
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(local_address)

# 定义send命令，发送send里面的指令给Telo无人机
def send(message):
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

# 定义receive命令，循环接收来自Tello的信息
def receive():
  while True:
    try:
      response, ip_address = sock.recvfrom(1024)
      print(response)
      out = response.decode(encoding='utf-8').replace(';',';\n') 
      #print("Tello state:\n",out)
      print("Received message: " + response.decode(encoding='utf-8'))
    except Exception as e:
      sock.close()
      print("Error receiving: " + str(e))
      break
      
# 开始一个监听线程，利用receive命令持续监控无人机发回的信号
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

# 告诉用户做什么
print('input Tello SDK指令，初始命令command，输入“quit”结束程式')
print("acceleration? /go x y z speed/takeoff/land")

# 无限循环等待指令输入直到输入“quit”或ctrl-c
while True:
  
  try:
    # 读取用户从键盘输入的指令
    if (sys.version_info > (3, 0)):
      message = input('')
    else:
      message = raw_input('')
    
    # 如果用户输入quit就结束循环并关闭socket
    if 'quit' in message:
      print("Program exited sucessfully")
      sock.close()
      break
    
    # 把指令发送给Tello
    send(message)
    
  # ctrl-c退出并关闭socket
  except KeyboardInterrupt as e:
    sock.close()
    break