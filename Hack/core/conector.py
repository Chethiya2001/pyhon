import socket

size = 4 *1024

class server_con:
    def  __init__(self):
        #create a TCP socket for server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def CreateConnection(self, ip="", port=12345):
        self.server_ip = ip
        self.server_port = port
        self.address = (self.server_ip, self.server_port)
        self.socket.bind(self.address)


    def Listen(self, backlog = 5 ):
        self.socket.listen(backlog)
    
    def AcceptConnection(self):
        self.client_conn, self.client_addr =  self.socket.accept()
        print("\t\t [+] connection establish with "+self.client_addr[0] +"on port "+str(self.client_addr[1]))
        return (self.client_conn, self.client_addr)
    
    def send_data(self, user_input):
        user_input_byte = bytes(user_input, "utf-8")

        self.client_conn.send(user_input_byte)
    
    def receive_data(self):
        receive_data_bytes = self.client_conn.recv(size)
        self.data = receive_data_bytes.decode("utf-8")
        return self.data
        
