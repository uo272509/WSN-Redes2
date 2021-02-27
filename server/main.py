import atexit
from flask import Flask, request, jsonify

from Exceptions import UnregisteredDeviceException
from Wrapper import PDBC, Log

app = Flask(__name__)
log = Log("requests.log")
db = PDBC('database.db')   # Connect/Create the database


@app.route("/getid", methods=["GET"])
def get_id():
    ip = request.remote_addr

    log.log("The device " + ip + " requested an ID")

    try:
        device_id = db.getID(ip)
        log.log("The device " + ip + " has the ID " + str(device_id))
    except UnregisteredDeviceException:
        device_id = db.getLastID() + 1
        db.newDevice(ip, device_id)
        log.log("The device " + ip + " has been given the ID \"" + str(device_id) + "\" and added to the database")

    return jsonify({'id': device_id}), 200


if __name__ == '__main__':
    atexit.register(db.close)  # On clean exit, close the connections
    atexit.register(log.close)  # On clean exit, close the log file

    app.run(host="0.0.0.0", port=8000)  # Use for testing
