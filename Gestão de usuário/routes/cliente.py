from flask import Blueprint, render_template, request
from peewee import IntegrityError
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    """ listar os clientes """
    clientes= Cliente.select()
    print('lista_clientes', clientes)
    return render_template('lista_clientes.html', clientes=clientes)
    

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ inserir os dados do cliente """
    data = request.json
    
    try:
        novo_usuario = Cliente.create(
            nome=data['nome'],
            email=data['email']
        )
        return render_template('item_cliente.html', cliente=novo_usuario)
    
    except IntegrityError:
        return "Erro: Este e-mail já está cadastrado.", 400
    

@cliente_route.route('/new')
def form_cliente():
    """  cadastrar um cliente """
    return render_template('form_cliente.html')
    

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ detalhes do cliente """
    
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente=cliente)
    

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """  editar um cliente """
    cliente = Cliente.get_by_id(cliente_id)

    return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ atualizar informacoes do cliente """
    data = request.json
    
    try:
        cliente_editado = Cliente.get_by_id(cliente_id)
        cliente_editado.nome = data['nome']
        cliente_editado.email = data['email']
        cliente_editado.save() 

        return render_template('item_cliente.html', cliente=cliente_editado)
    
    except IntegrityError:
        return "Erro: Não foi possível atualizar. Este e-mail já pertence a outro usuário.", 400


    

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):   
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return {'deleted': 'ok'}