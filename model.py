class Cartao:

    def __init__(self, numero, validade, cvv, limite, cliente):
        self.__numero = numero
        self.__validade = validade
        self.__cvv = cvv
        self.__limite = limite
        self.__cliente = cliente        
        self.__status = "ATIVO"

    def cancela(self):
        self.__status = "cancelado"

    def ativa(self):
        self.__status = "ativo"

    @property
    def numero(self):
        return self.__numero

    @property
    def validade(self):
        return self.__validade

    @property
    def cvv(self):
        return self.__cvv

    @property
    def limite(self):
        return self.__limite

    @property
    def cliente(self):
        return self.__cliente

    @property 
    def status(self):
        return self.__status
    
    
    @limite.setter
    def limite(self, novoValor):
         self.__limite = novoValor

class Compra:
    def __init__(self, valor, data, estabelecimento, categoria, cartao):
        self.__valor = valor
        self.__data = data
        self.__estabelecimento = estabelecimento
        self.__categoria = categoria
        self.__cartao = cartao

    def __str__(self):
        return f"Valor: {self.__valor}\n Data: {self.__data}\n Estabelecimento: {self.__estabelecimento}\n Número do Cartão: {self.__cartao.numero}"

    @property
    def valor(self):
        return self.__valor
 
class CompraCredito(Compra):
    def __init__(self, valor, data, estabelecimento, categoria, cartao, quantidade_parcelas):
        super().__init__(valor, data, estabelecimento, categoria, cartao)
        self.__quantidade_parcelas = quantidade_parcelas
        
    @property
    def valor(self):
        return super().valor*1.10
    
    @property
    def quantidade_parcelas(self):
        return self.__quantidade_parcelas
    
    @property
    def valor_parcela(self):
        return (super().valor/self.__quantidade_parcelas)*1.10