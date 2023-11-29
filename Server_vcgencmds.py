#Name : Huzaifa Patel
#Student No. : 100866869
#TPRG 2131 Assignment-2
#this is server file

import os
import socket
import json
import math
# Create a socket object
s = socket.socket()

# Localhost and port to bind to
host = '10.102.13.71'  # Change this to your desired IP address
port = 5000
s.bind((host, port))

# Listen for incoming connections
s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    # Get the Core Temperature, Voltage, and Clock Speed from Pi
    temperature = os.popen('vcgencmd measure_temp').readline().strip()
    voltage = os.popen('vcgencmd measure_volts core').readline().strip()
    clock_speed = os.popen('vcgencmd measure_clock arm').readline().strip()
    core_speed= os.popen('vcgencmd measure_clock core').readline().strip()
    voltage_sdram_c = os.popen('vcgencmd measure_volts sdram_c').readline().strip()
    # Create a dictionary with the collected data
    data_dict = {
        'Temperature': [temperature],
        'Voltage': [voltage],         
        'ClockSpeed': [clock_speed], 
        'CoreSpeed' : [core_speed],
        'Voltage_sdram_c' : [voltage_sdram_c] 
    }

    
    # Convert dictionary to JSON string
    json_data = json.dumps(data_dict)

    # Convert JSON string to bytes
    response = bytes(json_data, 'utf-8')
    
    # Send the response to the client
    c.send(response)

    # Close the connection
    c.close()