from random import randint
from pathlib import Path
from time import sleep
from settings import PROTO_MSG_PATH
import number_pb2


def loop():
    print("Running writer.py loop")
    while True:
        n = number_pb2.Number()
        n.value = randint(0,100)
        with open(PROTO_MSG_PATH, "wb") as proto_msg:
            proto_msg.write(n.SerializeToString())
        sleep(2)

loop()