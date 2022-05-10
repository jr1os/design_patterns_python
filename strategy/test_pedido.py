from decimal import Decimal
from pedido import Item
from pedido import Pedido, DescontoItemRepetido
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


@pytest.fixture
def pedido_item_repedito():
    pedido = Pedido()
    pedido.adicionar(Item('Mac', Decimal('100.00'), 10))
    return pedido


def test_total_sem_promocao(pedido_item_repedito):
    assert Decimal('1000.00') == pedido_item_repedito.total()


def test_total_com_promocao(pedido_item_repedito):
    desconto = DescontoItemRepetido()
    assert Decimal('900.00') == pedido_item_repedito.total(desconto)
