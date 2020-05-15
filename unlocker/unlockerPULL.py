import zmq

from unlockerUpdate import UnlockerUpdate

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://*:5558")

while True:
    print("等待解锁验证码…")
    message = socket.recv_string()
    r = message.split(',')
    if len(r) == 3:
        print("收到验证码...")
        print(r[0])
        print(r[1])
        print(r[2])
        UnlockerUpdate(r[0],r[1],r[2])
        print("验证码更新成功！")
    else:
        print("收到消息：%s"%message)
        print("收到验证码数据格式错误！")