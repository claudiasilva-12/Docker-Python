from flask import Flask

# Application initializations
app = Flask(__name__)

# settings
app.secret_key = "mysecretkey"

from contacts import contacts
app.register_blueprint(contacts)
