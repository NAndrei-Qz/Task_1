from praktikum.bun import Bun
import pytest


class TestBun:
    @pytest.mark.parametrize(
        'bun_name, bun_price',
        [
            ('White bun', 7),
            ('', 7),
            (None, 7),
            (999, 7)
        ]
    )
    def test_get_bun_name(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.get_name() == bun_name

    @pytest.mark.parametrize(
        'bun_name, bun_price',
        [
            ('black bun', 7),
            ('black bun', -7),
            ('black bun', 7.7),
            ('black bun', '7')
        ]
    )
    def test_get_bun_price(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.get_price() == bun_price

    def test_change_bun_name(self):
        bun = Bun('Pink bun', 18)
        bun.name = 'dry bun'
        assert bun.get_name() == 'dry bun'

    def test_change_bun_price(self):
        bun = Bun('sweet bun', 5)
        bun.price = 4
        assert bun.get_price() == 4

    