from decimal import Decimal
from pedido import Item
from pedido import Pedido
import pytest


def test_adicionar_item():
    mac = Item('Mac', Decimal('9.32'), 2)
    pedido = Pedido()
    pedido.adicionar(mac)
    assert 1 == len(pedido._itens)


@pytest.mark.parametrize(
        'itens,subtotal',
        [
            (
                [Item('Mac', Decimal('9.32'), 2)],
                '18.64'
            ),
            (
                [
                    Item('Mac', Decimal('9.32'), 2),
                    Item('Galaxy', Decimal('1.03'), 3)
                ],
                '21.73'
            ),
        ]
        )
def test_subtotal(itens, subtotal):
    pedido = Pedido()
    pedido.adicionar(*itens)
    assert Decimal(subtotal) == pedido.subtotal()
