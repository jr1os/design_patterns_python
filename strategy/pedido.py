from strategy.promocao import desconto_null_object


class Item:
    def __init__(self, descricao, preco, quantidade):
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def total(self):
        return self.preco * self.quantidade


class Pedido:
    def __init__(self):
        self._itens = []
        self._promocao = None

    def adicionar(self, *item):
        self._itens.extend(item)

    def subtotal(self):
        return sum(item.total() for item in self._itens)

    def total(self, promocao=desconto_null_object):
        """
        retorna o valor do subtotal depois de aplicado o valor da promocao
        :return: Decimal
        """
        return promocao.calcular_desconto(self)

    def soma_dos_items_com_quantidade_maior_que(self, limite):
        return sum(item.total() for item in self._itens if item.quantidade >= limite)
