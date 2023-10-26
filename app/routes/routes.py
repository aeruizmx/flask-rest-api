from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from models import Usuario, Pelicula
import bcrypt

blue_print = Blueprint('app', __name__)

# Ruta de inicio
@blue_print.route('/', methods=['GET'])
def inicio():
  return jsonify(respuesta='Rest API con Python, Flask y MySQL')

# Ruta de registro de usuario
@blue_print.route('/auth/registrar', methods=['POST'])
def registrar_usuario():
  try:
    #obtener el usuario
    usuario = request.json.get('usuario')
    #obtener la clave
    clave = request.json.get('clave')
    
    if not usuario or not clave:
      return jsonify(respuesta='Campos inválidos'), 400
    
    # Consultar la bd
    existe_usuario  = Usuario.query.filter_by(usuario=usuario).first()
    if existe_usuario:
      return jsonify(respuesta='Usuario ya existe'),400
    
    # Encriptamos clave de usuario
    clave_encriptada = bcrypt.hashpw(clave.encode('utf-8'), bcrypt.gensalt())
    
    #Creamos el modelo a guardar en BD
    nuevo_usuario = Usuario(usuario, clave_encriptada)
    db.session.add(nuevo_usuario)
    db.session.commit()
    
    return jsonify(respuesta='Usuario creado exitosamente'), 201
  except Exception:
    return jsonify(respuesta='Error en petición'), 500
  
@blue_print.route('/auth/login', methods=['POST'])
def iniciar_sesion():
  try:
    #obtener el usuario
    usuario = request.json.get('usuario')
    #obtener la clave
    clave = request.json.get('clave')
    
    if not usuario or not clave:
      return jsonify(respuesta='Campos inválidos'), 400
    
    # Consultar la bd
    existe_usuario  = Usuario.query.filter_by(usuario=usuario).first()
    if not existe_usuario:
      return jsonify(respuesta='Usuario no encontrado'),404
    
    es_clave_valida = bcrypt.checkpw(clave.encode('utf-8'), existe_usuario.clave.encode('utf-8'))
    # Validamos que sean iguales las claves
    if es_clave_valida:
      access_token = create_access_token(identity=usuario)
      return jsonify(access_token=access_token), 200
    return jsonify(respuesta='Clave o Usuario incorrecto'), 404
    
  except Exception:
      return jsonify(respuesta='Error en Petición'),500
