from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from modelos.usuario import Usuario

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/')
def listar_usuarios():
    usuarios = Usuario.obtener_todos()
    return render_template('usuarios.html', usuarios=usuarios)

@usuarios_bp.route('/crear', methods=['POST'])
def crear_usuario():
    nombre = request.form['nombre']
    correo = request.form['correo']
    contraseña = generate_password_hash(request.form['contraseña'])
    rol = request.form['rol']
    nuevo_usuario = Usuario(nombre, correo, contraseña, rol)
    nuevo_usuario.guardar()
    return redirect(url_for('usuarios.listar_usuarios'))

@usuarios_bp.route('/eliminar/<int:usuario_id>', methods=['POST'])
def eliminar_usuario(usuario_id):
    Usuario.eliminar(usuario_id)
    return redirect(url_for('usuarios.listar_usuarios'))
