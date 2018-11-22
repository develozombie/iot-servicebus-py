import string
import sys
import serial
import time
import os
import subprocess
from azure.servicebus import ServiceBusService, Message, Queue
# PUERTO_ARDUINO debe contener el valor de puerto serial que estas usando para tu Arduino
PUERTO_ARDUINO = 'COM3'
# BAUDIOS_ARDUINO debe contener los baudios que definiste en la apertura del serial
BAUDIOS_ARDUINO = 115200

bus_service = ServiceBusService(
    service_namespace='ti01usmp',
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='QN+1Qq1rsmmqTZj8ueQSGkaMYrsI9dACZI/fkT04OTw=')

arduino = serial.Serial(PUERTO_ARDUINO, BAUDIOS_ARDUINO, timeout=.1)
time.sleep(2)
subprocess.Popen(['C:\Program Files (x86)\Microsoft\Skype for Desktop\Skype.exe'])

while True:
    msg = bus_service.receive_queue_message('instruccion', peek_lock=False)
    if msg.body is not None:
        arduino.write(msg.body)
        raw = arduino.readline()
        print(raw)