class Validador:

    @staticmethod
    def nome_valido(nome):
        return nome is not None and len(nome.strip()) >= 5

    @staticmethod
    def cpf_valido(cpf):
        
        if cpf is None:
            return False

        cpf = ''.join(filter(str.isdigit, cpf))

        return len(cpf) == 11

    @staticmethod
    def telefone_valido(telefone):
        
        if telefone is None:
            return False

        telefone = ''.join(filter(str.isdigit, telefone))

        return len(telefone) in (10, 11)

    @staticmethod
    def email_valido(email):
        
        if email is None:
            return False

        return '@' in email
