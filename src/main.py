from cliente import Cliente
from banco import Banco
from conta_bancaria import ContaBancaria


# Criar banco
banco = Banco("Banco Universitario", 123)

# Criar clientes
cliente1 = Cliente(
    "Carlos Silva",
    "12345678901",
    "81999999999",
    "carlos@email.com"
)

cliente2 = Cliente(
    "Ana Souza",
    "98765432100",
    "81888888888",
    "ana@email.com"
)

cliente3 = Cliente(
    "Pedro Lima",
    "11122233344",
    "81777777777",
    "pedro@email.com"
)

# Criar contas
conta1 = ContaBancaria(
    101,
    cliente1,
    banco,
    1000
)

conta2 = ContaBancaria(
    102,
    cliente2,
    banco,
    500
)

conta3 = ContaBancaria(
    103,
    cliente3,
    banco,
    700
)

conta4 = ContaBancaria(
    104,
    cliente1,
    banco,
    200
)

# Registrar contas
banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)
banco.adicionar_conta(conta3)
banco.adicionar_conta(conta4)

# Depósitos
conta1.depositar(300)
conta2.depositar(100)

# Saques
conta3.sacar(200)
conta4.sacar(50)

# Impressão dos dados
print("=== RELATORIO DO BANCO ===")

print("Banco:", banco.get_nome())
print("Codigo:", banco.get_codigo())
print("Quantidade de contas:",
      banco.quantidade_contas())

saldo_total = 0

for conta in banco.listar_contas():

    print("\nTitular:",
          conta.get_titular().get_nome())

    print("CPF:",
          conta.get_titular().get_cpf())

    print("Conta:",
          conta.get_numero())

    print("Saldo: R$",
          conta.consultar_saldo())

    saldo_total += conta.consultar_saldo()

print("\nSaldo total do banco: R$",
      saldo_total)
