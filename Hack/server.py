import socket

# specify the server IP address and port number
SERVER_IP = ""
SERVER_PORT = 12345

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the specified IP address and port number
sock.bind((SERVER_IP, SERVER_PORT))

# listen for incoming connections (max backlog of 5)
sock.listen(5)

print(f'Server listening on {SERVER_IP}:{SERVER_PORT}...')

while True:
    # wait for a client to connect
    conn, addr = sock.accept()
    print(f'[+]Client connected from {addr[0]}:{addr[1]}')

    # send a welcome message to the client
    conn.send(b'Welcome to the server!')

    # receive data from the client
    data = conn.recv(1024)
    print(f'Received data: {data.decode()}')

    # send a response to the client
    conn.send(b'Response from the server')

    # close the connection
    conn.close()
