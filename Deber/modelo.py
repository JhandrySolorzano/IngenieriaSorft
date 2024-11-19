from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contraseña = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    def __init__(self, nombre, correo, contraseña, rol):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.rol = rol

    @staticmethod
    def obtener_todos():
        return Usuario.query.all()

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def eliminar(usuario_id):
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
