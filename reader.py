import number_pb2
from time import sleep
from settings import PROTO_MSG_PATH

def loop():
    print("Running reader.py loop")
    while True:
        sleep(1.5)
        with open (PROTO_MSG_PATH, "rb") as proto_msg:
            n = number_pb2.Number()
            n.ParseFromString(proto_msg.read())
            print(n.value)
        sleep(0.5)

loop()