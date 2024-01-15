from flask import jsonify, send_file, send_from_directory, Flask
import os

def get_frontend_path(filename):
    return send_from_directory(os.path.join(os.path.dirname(__file__), '..', 'frontend'), filename)