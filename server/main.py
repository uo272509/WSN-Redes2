import atexit
from flask import Flask, request, jsonify, json
import requests

from Exceptions import UnregisteredDeviceException
from Wrapper import PDBC, Log

app = Flask(__name__)

app.use_reloader = False
log = Log("requests.log")
db = PDBC('data.db')  # Connect/Create the database
server_dir=""


# PROTOCOL LAN
@app.route("/receive_data", methods=["POST"])
def receive_data():
    pass


# Protocol WAN
def resend_data(timestamp, machine, shard, sensorName, value, net):
    data = {
        [{"timestamp": timestamp,
          "machine": machine,
          "shard": shard,
          "type": sensorName,
          "value": value,
          "net": net
          }]
        }

    r = requests.post(server_dir, params=data)

@app.route("/getid", methods=["GET"])
def get_id():
    ip = request.remote_addr

    log.log("The device " + ip + " requested an ID.")

    try:
        device_id = db.getID(ip)
        log.log("The device " + ip + " has the ID " + str(device_id) + ".")
    except UnregisteredDeviceException:
        device_id = db.getLastID() + 1
        db.newDevice(ip, 0, device_id)
        log.log("The device " + ip + " has been given the ID \"" + str(device_id) + "\" and added to the database.")

    return jsonify({'id': device_id}), 200


@atexit.register
def close():  # This function will execute on clean exit
    db.close()  # Close the database connections
    log.log("Server is shutting down.")  # Close the log file
    log.close()  # Close the log file


if __name__ == '__main__':
    log.log("Server has started.")
    app.run(host="0.0.0.0", port=8000)  # Use for testing
