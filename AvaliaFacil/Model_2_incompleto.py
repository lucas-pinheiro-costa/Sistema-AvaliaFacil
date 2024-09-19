import pandas as pd
import streamlit as st
import datetime as dt
import re  # Import necessário para validar o formato de e-mail

class Usuario:
    def __init__(self, id, nome, email, senha, admin):
        # Validação do ID
        if not isinstance(id, int) or id <= 0:
            raise ValueError("\nID inválido, informe um número inteiro positivo.")

        # Validação do nome
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("\nO campo nome precisa ser preenchido com um valor válido.")
        
        # Validação do e-mail
        if not self.validar_email(email):
            raise ValueError("\nO campo e-mail precisa ser preenchido com um e-mail válido.")
        
        # Validação da senha (mínimo de 8 caracteres)
        if not isinstance(senha, str) or len(senha) < 8:
            raise ValueError("\nA senha deve ter pelo menos 8 caracteres.")
        
        #Conversão da variável booleana
        admin = admin.lower()
        if admin not in ['s', 'n']:
            raise ValueError("\nO campo admin precisa ser preenchido com S/s (para sim) ou N/n (para não).")
        admin = admin == 's'  # Conversão para booleano
        
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__admin = admin

    # Método para validar formato de e-mail
    def validar_email(self, email):
        padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(padrao_email, email) is not None
    
    # Getters e Setters
    def get_id(self):
        return self.__id
    
    def set_id(self, value):
        if isinstance(value, int) and value > 0:
            self.__id = value
        else:
            raise ValueError("ID inválido, deve ser um número inteiro positivo.")
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, value):
        if isinstance(value, str) and value.strip():
            self.__nome = value
        else:
            raise ValueError("O nome deve ser uma string não vazia.")
    
    def get_email(self):
        return self.__email
    
    def set_email(self, value):
        if self.validar_email(value):
            self.__email = value
        else:
            raise ValueError("Insira um e-mail válido.")
    
    def get_senha(self):
        return self.__senha
    
    def set_senha(self, value):
        if isinstance(value, str) and len(value) >= 8:
            self.__senha = value
        else:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")
    
    def get_admin(self):
        return self.__admin
    
    def set_admin(self, value):
        value = value.lower()
        if value not in ['s', 'n']:
            raise ValueError("\nO campo admin precisa ser preenchido com S/s (para sim) ou N/n (para não).")
        self.__admin = value == 's'  # Conversão para booleano

    def __str__(self):
        return f"\nINFORMAÇOES DO USUÁRIO:\n\tID: {self.__id}\n\tNome: {self.__nome}\n\tE-mail: {self.__email}\n\tAdmin: {self.__admin}\n"