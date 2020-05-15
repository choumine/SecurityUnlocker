import zmq
import time

def UnlockerPush(imei, timestamp):
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind("tcp://*:5557")
    m = "%s,%s"%(imei, timestamp)
    socket.send_string(m)
    print("Send message: %s"%m)