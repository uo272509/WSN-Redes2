import atexit
from flask import Flask

from Wrapper import PDBC

app = Flask(__name__)

if __name__ == '__main__':
    db = PDBC('database.db')  # Connect/Create the database
    atexit.register(db.close)  # On clean exit, close the connections

    app.run(host="0.0.0.0", port=8000)  # Use for testing
