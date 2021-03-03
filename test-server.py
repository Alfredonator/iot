import socket

def start(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(10)
    print('waiting for connection...')
    connection, client_addr = server_socket.accept()
    print('Connection established')
    while (True):
        try:
            rec = connection.recv(1024).decode()
            if (rec == 'unbreak'): print(rec)
        except Exception as e:
            print(e)
            raise


if __name__ == '__main__':
    start(socket.gethostbyname(socket.gethostname()), 88)
