import logging
from opcua import Client


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    client = Client("opc.tcp://localhost:4841/freeopcua/server/")
    client.application_uri = "URN:192.168.41.11"
    client.secure_channel_timeout = 10000
    client.session_timeout = 10000
    try:
        client.connect()
        root = client.get_root_node()
        objects = client.get_objects_node()
        print("childs og objects are: ", objects.get_children()[1].get_children())

        myint = client.get_node("ns=2;i=2")
        print("variabile intera: ",myint.get_value())
        print(myint.get_data_type_as_variant_type())

        myfloat = client.get_node("ns=2;i=3")
        print("variabile float: ",myfloat.get_value())
        print(myfloat.get_data_type_as_variant_type())
        
    finally:
        client.disconnect()
