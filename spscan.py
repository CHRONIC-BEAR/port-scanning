#single port scanner
import socket

IP_ADDRESS = '192.168.1.254' #IP address of the device we would like to port scanning
PORT = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #socket object
    try:
        s.connect((IP_ADDRESS, PORT)) #tries to connect using IP_ADDRESS and PORT
        print(f'port {PORT} is now open and listening')
    except: #if it fails (times out, etc.)
        print(f'failed to connect to port {PORT}')
