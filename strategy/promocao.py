from __future__ import absolute_import, unicode_literals
from decimal import Decimal
from abc import ABC, abstractmethod


class Desconto(ABC):
    """Classe base de todos descontos"""
    @abstractmethod
    def calcular_desconto(self, pedido):
        """
        deve calcular o valor de desconto de acordo com o pedido
        """


class _DescontoNullObject:
    def calcular_desconto(self, pedido):
        return pedido.subtotal()


desconto_null_object = _DescontoNullObject()


class _DescontoItemRepetido(Desconto):
    """
    fornece 10% de desconto em cima de items com quantidade igual ou
    superior a 10
    """

    def calcular_desconto(self, pedido):
        desconto = pedido.soma_dos_items_com_quantidade_maior_que(10)
        desconto = desconto * Decimal('0.10')
        return pedido.subtotal() - desconto


desconto_item_repetido = _DescontoItemRepetido()


class _DescontoGrandePedido(Desconto):
    """Desconto de 5% pedido maiores que 10.000"""
    def calcular_desconto(self, pedido):
        subtotal = pedido.subtotal()
        if subtotal < 10000:
            return subtotal
        return subtotal * Decimal('0.95')


desconto_grande_pedido = _DescontoGrandePedido()
