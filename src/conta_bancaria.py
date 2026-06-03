class ContaBancaria:

    def __init__(self,
                 numero,
                 titular,
                 banco,
                 saldo_inicial):

        self.numero = 0
        self.saldo = 0
        self.titular = titular
        self.banco = banco

        if numero > 0:
            self.numero = numero

        if saldo_inicial >= 0:
            self.saldo = saldo_inicial

    def depositar(self, valor):
        
        if valor > 0:
            self.saldo += valor
    
    def sacar(self, valor):
        
        if valor <= 0:
            return False

        if valor > self.saldo:
            return False

        self.saldo -= valor
        return True
    
    def consultar_saldo(self):
        return self.saldo
    
    def get_numero(self):
        return self.numero
    
    def get_titular(self):
        return self.titular
    
    def get_banco(self):
        return self.banco
    
    def esta_ativa(self):
        return self.saldo > 0
