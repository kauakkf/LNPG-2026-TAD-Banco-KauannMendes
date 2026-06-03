from validador import Validador

class Cliente:

    def __init__(self, nome, cpf,
                 telefone=None,
                 email=None):
                   
        self.nome = None
        self.cpf = None
        self.telefone = None
        self.email = None

        if Validador.nome_valido(nome):
            self.nome = nome

        if Validador.cpf_valido(cpf):
            self.cpf = cpf

        if telefone is not None:
            if Validador.telefone_valido(telefone):
                self.telefone = telefone

        if email is not None:
            if Validador.email_valido(email):
                self.email = email
    
    def get_nome(self):
        return self.nome
    
    def get_cpf(self):
        return self.cpf
    
    def get_telefone(self):
        return self.telefone
    
    def get_email(self):
        return self.email
    
    def alterar_telefone(self, telefone):
        
        if Validador.telefone_valido(telefone):
            self.telefone = telefone
    
    def alterar_email(self, email):
        if Validador.email_valido(email):
            self.email = email
