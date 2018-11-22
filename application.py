import sys
import logging
import datetime
import time
import os
from azure.servicebus import ServiceBusService, Message, Queue
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

bus_service = ServiceBusService(
    service_namespace='ti01usmp',
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='QN+1Qq1rsmmqTZj8ueQSGkaMYrsI9dACZI/fkT04OTw=')

@app.route("/")
def hello():
    return render_template(
        'tabla.html')

@app.route("/funcion/<string:q>/")
def funcion(q):
    msg = Message(q)
    bus_service.send_queue_message('instruccion', msg)
    return "OK"

if __name__ == "__main__":
    app.run()