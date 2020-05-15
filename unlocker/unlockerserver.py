#
#   解锁工具服务器程序，回应客户端请求
#   1、收到“Y”，查找数据库，如果有待解锁数据，回复“Y”，如果没有待解锁数据，回复“N”。
#   2、收到“G”，返回带解锁数据，格式“imei,timestamp”。
#   3、收到解锁码,格式“imei,timestamp,unlockcode”，回复“O”。
#   4、收到其他消息，回复“E”。
#

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  等待客户端消息
    message = socket.recv_string()
    print("收到客户端消息: %s" %message)

    #  检查客户端消息
    if message == 'Y':
        socket.send_string('Y')
    elif message == 'G':
        socket.send_string('1,2')
    else:
        r = message.split(',')
        if len(r) == 3:
            print(r[0])
            print(r[1])
            print(r[2])
            socket.send_string('O')
        else:
            socket.send_string('E')
