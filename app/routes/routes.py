from flask import Blueprint, request, jsonify

blue_print = Blueprint('app', __name__)

# Ruta de inicio
@blue_print.route('/', methods=['GET'])
def inicio():
  return '<h1>Flask API </h1>'
