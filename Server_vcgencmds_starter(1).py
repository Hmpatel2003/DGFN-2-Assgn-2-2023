# This server runs on Pi, sends Pi's your 4 arguments from the vcgencmds, sent as Json object.

# details of the Pi's vcgencmds - https://www.tomshardware.com/how-to/raspberry-pi-benchmark-vcgencmd
# more vcgens on Pi 4, https://forums.raspberrypi.com/viewtopic.php?t=245733
# more of these at https://www.nicm.dev/vcgencmd/

import socket
import os, time
import json

s = socket.socket()
host = '' # Localhost
port = 5000
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    # Get the Core Temperature, Voltage, and Clock Speed from Pi
    temperature = os.popen('vcgencmd measure_temp').readline().strip()
    voltage = os.popen('vcgencmd measure_volts core').readline().strip()

    data_dict = {
        'Temperature': [temperature],
        'Voltage': [voltage]
        }

# Convert dictionary to JSON string
    json_data = json.dumps(data_dict)

    # Convert JSON string to bytes
    response = bytes(json_data, 'utf-8')
    
    # Send the response to the client
    c.send(response)

    # Close the connection
    c.close()
