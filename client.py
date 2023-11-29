#Name : Huzaifa Patel
#Student No. : 100866869
#TPRG 2131 Assignment-2
#This is client file

import json
import socket
s = socket.socket()
host = '10.102.13.71'
port = 5000
s.connect((host, port))

received_data = s.recv(1024)# Receive data from the server

decoded_data = json.loads(received_data.decode())
# Decode the bytes and load JSON data into a dictionary

# Print the key-value pairs
for key, value in decoded_data.items():
    print("{}: {}".format(key, value))

# Close the connection
s.close()

