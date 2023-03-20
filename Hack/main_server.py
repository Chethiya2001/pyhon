from core.conector import server_con


if __name__ == "__main__":
    my_socket = server_con()
    my_socket.CreateConnection("", 12345)

    my_socket.Listen()

    my_connection, _ = my_socket.AcceptConnection()

    my_connection.close()
    