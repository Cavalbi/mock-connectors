import uuid
from threading import Thread
import copy
import logging
from datetime import datetime
import time
from math import sin
import sys
import signal
from random import seed
from random import randint
from opcua.ua import NodeId, NodeIdType
from opcua import ua, uamethod, Server

# seed random number generator
seed(1)
sys.path.insert(0, "..")

class FloatUpdater(Thread):
    def __init__(self, var):
        Thread.__init__(self)
        self._stopev = False
        self.var = var

    def stop(self):
        self._stopev = True

    def run(self):
        while not self._stopev:
            v = sin(time.time() / 10)
            self.var.set_value(v)
            time.sleep(0.1)

class IntUpdater(Thread):
    def __init__(self, var):
        Thread.__init__(self)
        self._stopev = False
        self.var = var

    def stop(self):
        self._stopev = True

    def run(self):
        while not self._stopev:
            v = randint(0, 1000)
            self.var.set_value(v)
            time.sleep(0.1)

if __name__ == "__main__":
    # optional: setup logging
    logging.basicConfig(level=logging.WARN)
    

    # now setup our server
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4841/freeopcua/server/")
    server.set_server_name("FreeOpcUa Example Server")
    # set all possible endpoint policies for clients to connect through
    server.set_security_policy([
                ua.SecurityPolicyType.NoSecurity,
                ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt,
                ua.SecurityPolicyType.Basic256Sha256_Sign])

    # setup our own namespace
    uri = "URN:192.168.41.11"
    idx = server.register_namespace(uri)

    # create directly some objects and variables
    myobj = server.nodes.objects.add_object(idx, "MyObject")
    myint = myobj.add_variable(idx, "MyInt", 7,ua.VariantType.UInt32)
    myfloat = myobj.add_variable(idx, "MyFloat", 0, ua.VariantType.Float)

    # starting!
    server.start()
    print("Available loggers are: ", logging.Logger.manager.loggerDict.keys())
    fup = FloatUpdater(myfloat)  # just  a stupide class update a variable
    fup.start()
    iup = IntUpdater(myint)  # just  a stupide class update a variable
    iup.start()
   