import socket
import ssl
import time

class TLSClientConnection:
    ca_certs = ''
    clt_cert = ''
    clt_key = ''

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS)
        self.ssl_context.verify_mode = ssl.CERT_REQUIRED
        self.ssl_context.load_cert_chain(certfile=self.clt_cert, keyfile=self.clt_key)
        self.client_socket = socket.socket()
        self.secure_socket = None
        self.msg_buffer = []

    #TODO make it pretty even when not connected
    def connect(self):
        try:
            self.secure_socket = self.ssl_context.wrap_socket(self.client_socket)
            self.secure_socket.connect((self.ip, self.port))
        except Exception as e:
            print('Error connecting: ', e)
            raise

    def write_msg(self, msg):
        try:
            self.secure_socket.send(msg.encode())
        except Exception as e:
            print('Error sending: ', e)

    def cert_validation(self):
        server_cert = self.secure_socket.getpeercert()

    def server_cert_validation(self, crt):
        subject = dict(item[0] for item in crt['subject'])
        commonName = subject['commonName']
        if not crt:
            raise Exception("Unable to retrieve server certificate")

        if commonName != 'edo_server':
            raise Exception("Incorrect common name in server certificate")

    def validate_crt_time(self, crt):
        notAfterTimestamp = ssl.cert_time_to_seconds(crt['notAfter'])
        notBeforeTimestamp = ssl.cert_time_to_seconds(crt['notBefore'])
        currentTimeStamp = time.time()

        if currentTimeStamp > notAfterTimestamp:
            raise Exception("Expired server certificate")

        if currentTimeStamp < notBeforeTimestamp:
            raise Exception("Server certificate not yet active")


def start_conn(ip, port):
    tls_conn = TLSClientConnection(ip, port)
    tls_conn.connect()
    print('Connection established!')
    try:
        print('Whatever activity we need')
    finally:
        tls_conn.close()


