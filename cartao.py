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
