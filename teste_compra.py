from model import Cartao, Compra, CompraCredito

visa = Cartao("1234 5678 9000 0000", "12/30", "123", 50000.00, "Fernando")
mastercard = Cartao("0000 0012 3456 7899", "12/23", "222", 1000.00, "Daniela")
farmacia = Compra(34.95, "23/09/2023", "drogasil", "Antiinflamatório", visa)
restaurante = Compra(233.24, "16/09/2023", "Outback", "refeições", mastercard)
supermercado = Compra(94.75, "24/09/2023", "Extra", "produtos de limpeza", visa)

#print(farmacia)
#print(restaurante)
#print(supermercado)

compra_parcela = CompraCredito(233.24, "16/09/2023", "Outback", "refeições", mastercard, 3)
#print(compra_parcela)
#print("Valor da parcela: %.2f"% compra_parcela.valor_parcela)
#print("%.2f"% compra_parcela.valor)

fatura = [farmacia, restaurante, supermercado, compra_parcela]
total = 0
for item in fatura:
    total += item.valor

print(f"Valor total fatura: {total}")  