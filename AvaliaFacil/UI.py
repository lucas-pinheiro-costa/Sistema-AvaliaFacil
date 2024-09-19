from classes import *

usuarios = []


def create_usuario(id, nome, senha, admin):
    usuario = Usuario(id, nome, senha, admin)
    usuarios.append(usuario)


def read_usuarios():
    for usuario in usuarios:
        print(f"ID: {usuario.get_id()}, Nome: {usuario.get_nome()}, Admin: {usuario.get_admin()}")


def update_usuario(id, nome=None, senha=None, admin=None):
    for usuario in usuarios:
        if usuario.get_id() == id:
            if nome:
                usuario.set_nome(nome)
            if senha:
                usuario.set_senha(senha)
            if admin is not None:
                usuario.set_admin(admin)
            return
    raise ValueError("Usuário não encontrado.")

def delete_usuario(id):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario.get_id() != id]


estabelecimentos = []

def create_estabelecimento(id, nome, endereco, descricao, tipo):
    estabelecimento = Estabelecimento(id, nome, endereco, descricao, tipo)
    estabelecimentos.append(estabelecimento)

def read_estabelecimentos():
    for estabelecimento in estabelecimentos:
        print(f"ID: {estabelecimento.get_id()}, Nome: {estabelecimento.get_nome()}, Endereço: {estabelecimento.get_endereco()}, Descrição: {estabelecimento.get_descricao()}, Tipo: {estabelecimento.get_tipo()}")

def update_estabelecimento(id, nome=None, endereco=None, descricao=None, tipo=None):
    for estabelecimento in estabelecimentos:
        if estabelecimento.get_id() == id:
            if nome:
                estabelecimento.set_nome(nome)
            if endereco:
                estabelecimento.set_endereco(endereco)
            if descricao:
                estabelecimento.set_descricao(descricao)
            if tipo:
                estabelecimento.set_tipo(tipo)
            return
    raise ValueError("Estabelecimento não encontrado.")

def delete_estabelecimento(id):
    global estabelecimentos
    estabelecimentos = [estabelecimento for estabelecimento in estabelecimentos if estabelecimento.get_id() != id]


clientes = []

def create_cliente(id, email, telefone):
    cliente = Cliente(id, email, telefone)
    clientes.append(cliente)

def read_clientes():
    for cliente in clientes:
        print(f"ID: {cliente.get_id()}, Email: {cliente.get_email()}, Telefone: {cliente.get_telefone()}")

def update_cliente(id, email=None, telefone=None):
    for cliente in clientes:
        if cliente.get_id() == id:
            if email:
                cliente.set_email(email)
            if telefone:
                cliente.set_telefone(telefone)
            return
    raise ValueError("Cliente não encontrado.")

def delete_cliente(id):
    global clientes
    clientes = [cliente for cliente in clientes if cliente.get_id() != id]

avaliacoes = []

def create_avaliacao(id, data, qualidadedoproduto, tempoespera, limpeza, atendimento, buffet, cardapio, ambiente, preco, nota, comentario, anonimo):
    avaliacao = Avaliacao(id, data, qualidadedoproduto, tempoespera, limpeza, atendimento, buffet, cardapio, ambiente, preco, nota, comentario, anonimo)
    avaliacoes.append(avaliacao)

def read_avaliacoes():
    for avaliacao in avaliacoes:
        print(f"ID: {avaliacao.get_id()}, Data: {avaliacao.get_data()}, Qualidade do Produto: {avaliacao.get_qualidadedoproduto()}, Tempo de Espera: {avaliacao.get_tempoespera()}, Limpeza: {avaliacao.get_limpeza()}, Atendimento: {avaliacao.get_atendimento()}, Buffet: {avaliacao.get_buffet()}, Cardápio: {avaliacao.get_cardapio()}, Ambiente: {avaliacao.get_ambiente()}, Preço: {avaliacao.get_preco()}, Nota: {avaliacao.get_nota()}, Comentário: {avaliacao.get_comentario()}, Anônimo: {avaliacao.get_anonimo()}")

def update_avaliacao(id, data=None, qualidadedoproduto=None, tempoespera=None, limpeza=None, atendimento=None, buffet=None, cardapio=None, ambiente=None, preco=None, nota=None, comentario=None, anonimo=None):
    for avaliacao in avaliacoes:
        if avaliacao.get_id() == id:
            if data:
                avaliacao.set_data(data)
            if qualidadedoproduto:
                avaliacao.set_qualidadedoproduto(qualidadedoproduto)
            if tempoespera:
                avaliacao.set_tempoespera(tempoespera)
            if limpeza:
                avaliacao.set_limpeza(limpeza)
            if atendimento:
                avaliacao.set_atendimento(atendimento)
            if buffet:
                avaliacao.set_buffet(buffet)
            if cardapio:
                avaliacao.set_cardapio(cardapio)
            if ambiente:
                avaliacao.set_ambiente(ambiente)
            if preco:
                avaliacao.set_preco(preco)
            if nota:
                avaliacao.set_nota(nota)
            if comentario:
                avaliacao.set_comentario(comentario)
            if anonimo is not None:
                avaliacao.set_anonimo(anonimo)
            return
    raise ValueError("Avaliação não encontrada.")

def delete_avaliacao(id):
    global avaliacoes
    avaliacoes = [avaliacao for avaliacao in avaliacoes if avaliacao.get_id() != id]


feedbacks = []

def create_feedback(id, comentario):
    feedback = Feedback(id, comentario)
    feedbacks.append(feedback)

def read_feedbacks():
    for feedback in feedbacks:
        print(f"ID: {feedback.get_id()}, Comentário: {feedback.get_comentario()}")

def update_feedback(id, comentario=None):
    for feedback in feedbacks:
        if feedback.get_id() == id:
            if comentario:
                feedback.set_comentario(comentario)
            return
    raise ValueError("Feedback não encontrado.")

def delete_feedback(id):
    global feedbacks
    feedbacks = [feedback for feedback in feedbacks if feedback.get_id() != id]