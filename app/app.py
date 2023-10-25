from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
  return '<h1>Flask API </h1>'

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=8080)