from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Usuario, db

hello_bp = Blueprint('hello', __name__)
hello_name = Blueprint('hello_name', __name__)

@hello_bp.route('/')
def index():
    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)

@hello_name.route('/sobre')
def sobre():
    return render_template('sobre.html')

@hello_bp.route('/novo_usuario', methods=["POST"])
def novo_usuario():
    username = request.form['nome']
    novo_usuario = Usuario(username=username)
    db.session.add(novo_usuario)
    db.session.commit()
    return redirect('/')

@hello_bp.route('/deletar_usuario/<int:usuario_id>', methods=["POST"])
def deletar_usuario(usuario_id):
    usuario = Usuario.query.get_or_404(usuario_id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('hello.index'))

@hello_bp.route('/editar_usuario/<int:usuario_id>', methods=["POST"])
def editar_usuario(usuario_id):
    usuario = Usuario.query.get_or_404(usuario_id)
    # Check if 'novo_usuario' key exists to avoid a KeyError
    if 'novo_usuario' in request.form:
        usuario.username = request.form['novo_usuario']
        db.session.commit()
    return redirect(url_for('hello.index'))