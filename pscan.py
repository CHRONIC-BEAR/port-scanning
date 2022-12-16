#multiple port scanner
import socket

IP_ADDRESS = '192.168.1.254'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #socket object
    for port in range(50, 150): #for every integer between 100 and 150 (port)
        try:
            s.connect((IP_ADDRESS, port)) #port is equal to every number between 100 and 150
            print(f'port {port} is open and listening')
        except:
            print(f'port {port} is closed')
#this try statement tries to connect to every port between 100 and 150

#this program is currently experiencing an error where it accurately acknowledges only the first open port it scans, but none thereafter
