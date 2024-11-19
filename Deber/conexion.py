from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controladores.usuarios import usuarios_bp

app = Flask(__name__)
app.secret_key = "123456789"

# Configuración de MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456789@localhost/gestion_usuarios'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db = SQLAlchemy(app)

# Registrar el módulo de usuarios
app.register_blueprint(usuarios_bp, url_prefix='/root')

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
