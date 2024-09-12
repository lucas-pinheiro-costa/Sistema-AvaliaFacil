#acrescentar classes e utilizar conceito de herança
#iniciar front no streamlit 

import pandas as pd
import streamlit as st

class Usuario:
    def __init__(self, id, nome, senha, admin):
        self.__id = id
        self.__nome = nome
        self.__senha = senha 
        self.__admin = admin 

    def get_id(self):
        return self.__id
    def set_id(self, value):
        if self.__id > 0: 
            self.__id = value
        else: raise ValueError("Digite um ID válido.\n")
    
    def get_nome(self):
        return self.__nome
    def set_nome(self, value):
        if isinstance(value, str):
            self.__nome = value 
    
    def get_senha(self):
        return self.__senha 
    def set_senha(self, value):
        if len(value) >= 6:
            self.__senha = value
        else: raise ValueError("A senha deve ter pelo menos 8 caracteres. \n")
    
    def get_admin(self):
        return self.__admin
    def set_admin(self, value):
        if isinstance(value, bool):
            self.__admin = value
        else: raise ValueError("O admin é inválido")
        
class Estabelecimento:
    def __init__(self, id, nome, endereco, descricao, tipo):
        self.__id = id
        self.__nome = nome 
        self.__endereco = endereco
        self.__descricao = descricao 
        self.__tipo = tipo 
        
    def get_id(self):
        return self.__id 
    def set_id(self, value):
        if value > 0: 
            self.__id = value
        else: raise ValueError("Digite um ID válido.\n")
    
    def get_nome(self):
        return self.__nome
    def set_nome(self, value):
        if isinstance(value, str):
            self.__nome = value
        else: raise ValueError("O nome deve ser uma string.\n") 
   
    def get_endereco(self):
        return self.__endereco
    def set_endereco(self, value):
        if isinstance(self, value):
            self.__endereco = value
        else: raise ValueError("O endereço deve ser uma string.\n") 
    
    def get_descricao(self):
        return self.__descricao
    def set_descricao(self, value):
        if isinstance(self, value):
            self.__descricao = value
        else: raise ValueError("A descrição deve ser uma string.\n") 
    
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self, value):
        if isinstance(self, value):
            self.__tipo = value
        else: raise ValueError("O tipo deve ser uma string.\n") 
    
    def set_usuario(self, value):
        if isinstance(value, Usuario):
            self.__usuario = value  
        else: raise ValueError("O usuário deve ser uma instância da classe Usuario.")

class Cliente:
    def __init__(self, id, email, telefone):
        self.__id = id
        self.__email = email 
        self.__telefone = telefone 
    
    def get_id(self):
        return self.__id 
    def set_id(self, value):
        if value >= 0: 
            self.__id = value 
        else: raise ValueError("Digite um ID válido.\n") 
    
    def get_email(self):
        return self.__email 
    def set_email(self, value):
        if isinstance(value, str):
            self.__email = value
        else: raise ValueError("O email precisa ser uma string.")

class Avaliacao:
    def __init__(self, id, data, qualidadedoproduto, tempoespera, limpeza, atendimento, buffet, cardapio, ambiente, preco, nota, comentario, anonimo):
        self.__id = id
        self.__data = data
        self.__qualidadedoproduto = qualidadedoproduto
        self.__tempoespera = tempoespera
        self.__limpeza = limpeza
        self.__atendimento = atendimento
        self.__buffet = buffet
        self.__cardapio = cardapio 
        self.__ambiente = ambiente 
        self.__preco = preco
        self.__nota = nota 
        self.__comentario = comentario
        self.__anonimo = anonimo 

    def get_id(self):
        return self.__id 
    def set_id(self, value): 
        










class Feedback: 
    def __init__(self, id, comentario):
        self.__id = id
        self.__comentario = comentario 
    
    def get_id(self):
        return self.__id
    def set_id(self, value):
        if value >= 0: 
            self.__id = value 
        else: raise ValueError("Digite um ID válido.")
    
    def get_comentario(self):
        return self.__comentario 
    def set_comentario(self, value):
        if isinstance(value, str):
            self.__comentario = value 
        else: raise ValueError("O comentário precisa ser uma string.")

    def set_IdEstabelecimento(self, value):
        if isinstance(value, Estabelecimento):
               self.__value = value

    def set_IdAvaliacao(self, value):
        if isinstance(value, Avaliacao):
               self.__value = value