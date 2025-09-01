from flask import Blueprint

hello_bp = Blueprint('hello',__name__)
hello_name = Blueprint('hello_name',__name__)

@hello_bp.route('/')
def index():
    return 'Olá, Mundo!'

@hello_name.route('/sobre')
def index():
    return 'Olá, Rodrigo!'