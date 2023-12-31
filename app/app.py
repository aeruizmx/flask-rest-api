from flask import Flask
from database import db
from sqlalchemy_utils import create_database, database_exists
from routes.routes import blue_print
from flask_jwt_extended import JWTManager
import datetime


app = Flask(__name__)

# Base de datos
db_usuario = 'root'
db_clave = 'root'
db_host = 'localhost'
db_nombre = 'db_api_python'

DB_URL = f'mysql+pymysql://{db_usuario}:{db_clave}@{db_host}/{db_nombre}'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = "eyJhbGciOiJIUzI1NiJ9"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=12)

# JWT
jwt = JWTManager(app)

# Inicializamos SQLAlchemy
db.init_app(app)

# Instanciamos rutas
app.register_blueprint(blue_print)

# Crear la base de datos
with app.app_context():
  if not database_exists(DB_URL):
    create_database(DB_URL)
  db.create_all()
    

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=8080)