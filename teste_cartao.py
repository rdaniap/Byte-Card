from cartao import Cartao

visa = Cartao("1234 5678 9000 0000", "12/30", "123", 50000.00, "Fernando")
mastercard = Cartao("0000 0012 3456 7899", "12/23", "222", 1000.00, "Daniela")
visa.cancela()
mastercard.cancela()

visa.limite = 5000.00
mastercard.limite = 7000.00

print(f"Nome do cliente: {visa.cliente}\n Cartão Nº: {visa.numero}\n limite: {visa.limite}\n status: {visa.status}")
print(f"Nome do cliente: {mastercard.cliente}\n Cartão Nº: {mastercard.numero}\n limite: {mastercard.limite}\n status: {mastercard.status}")