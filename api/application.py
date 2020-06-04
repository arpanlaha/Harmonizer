from flask import Flask, request, jsonify
from flask_cors import CORS
from __app__.views import harmony


app = Flask(__name__)
CORS(app)
app.register_blueprint(harmony)
