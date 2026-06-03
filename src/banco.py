class Banco:

    def __init__(self, nome, codigo):
        
        self.nome = None
        self.codigo = 0
        self.contas = []

        if nome is not None and len(nome) >= 3:
            self.nome = nome

        if codigo > 0:
            self.codigo = codigo

    def adicionar_conta(self, conta):
        
        if self.buscar_conta(conta.get_numero()) is not None:
            return False

        self.contas.append(conta)
        return True

    def remover_conta(self, numero):
        
        conta = self.buscar_conta(numero)

        if conta is None:
            return False

        self.contas.remove(conta)
        return True
    
    def buscar_conta(self, numero):
        
        for conta in self.contas:

            if conta.get_numero() == numero:
                return conta

        return None
    
    def quantidade_contas(self):
        return len(self.contas)
    
    def listar_contas(self):
        return self.contas

    def get_nome(self):
        return self.nome

    def get_codigo(self):
        return self.codigo
