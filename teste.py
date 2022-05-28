from models.cliente import Cliente
from models.conta import Conta

cliente1 = Cliente("João Gomez", "joao@gmail.com", "34556789000", "12/05/1980")
cliente2 = Cliente("Gabriela Farias", "gabriela@gmail.com", "23145623412", "31/01/2000")

#print(cliente1)
#print(cliente2)

conta1 = Conta(cliente1)
conta2 = Conta(cliente2)

print(conta1)
print(conta2)