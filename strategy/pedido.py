from decimal import Decimal
from abc import ABC, abstractmethod


class Item:
    def __init__(self, descricao, preco, quantidade):
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.preco * self.quantidade


class Pedido:
    def __init__(self):
        self._itens = []
        self._promocao = None

    def adicionar(self, *item):
        self._itens.extend(item)

    def subtotal(self):
        return sum(item.subtotal() for item in self._itens)

    def total(self, promocao=None):
        """
        retorna o valor do subtotal depois de aplicado o valor da promocao
        :return: Decimal
        """
        if promocao is None:
            return self.subtotal()
        return promocao.calcular_desconto(self)

    def soma_dos_items_com_quantidade_maior_que(self, limite):
        return sum(item.total() for item in self._itens if item.quantidade >= limite)


class Desconto(ABC):
    """Classe base de todos descontos"""
    @abstractmethod
    def calcular_desconto(self, pedido: Pedido):
        """
        deve calcular o valor de desconto de acordo com o pedido
        """


class DescontoItemRepetido(Desconto):
    """
    fornece 10% de desconto em cima de items com quantidade igual ou
    superior a 10
    """

    def calcular_desconto(self, pedido: Pedido):
        desconto = pedido.soma_dos_items_com_quantidade_maior_que(10)
        desconto *= Decimal('0.10')
        return pedido.subtotal() - desconto
