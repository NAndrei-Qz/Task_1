import pytest


class TestBurger:

    def test_set_buns(self, burger, mock_red_bun):
        burger.set_buns(mock_red_bun)
        assert burger.bun == mock_red_bun

    def test_add_ingredient(self, burger, mock_ingredient_sour_cream):
        burger.add_ingredient(mock_ingredient_sour_cream)
        assert burger.ingredients == [mock_ingredient_sour_cream]
        
    def test_remove_ingredient(self, burger, mock_ingredient_sour_cream, mock_ingredient_dinosaur):
        burger.add_ingredient(mock_ingredient_sour_cream)
        burger.add_ingredient(mock_ingredient_dinosaur)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_ingredient_dinosaur]

    def test_move_ingredient(self, burger, mock_ingredient_sour_cream, mock_ingredient_dinosaur):
        burger.add_ingredient(mock_ingredient_sour_cream)
        burger.add_ingredient(mock_ingredient_dinosaur)
        burger.move_ingredient(0,1)
        assert burger.ingredients == [mock_ingredient_dinosaur, mock_ingredient_sour_cream]

    def test_get_price(self, burger, mock_red_bun, mock_ingredient_sour_cream, mock_ingredient_dinosaur):
        burger.bun = mock_red_bun
        burger.ingredients = [mock_ingredient_sour_cream, mock_ingredient_dinosaur]
        mock_red_bun.get_price.return_value = 666
        mock_ingredient_sour_cream.get_price.return_value = 101
        mock_ingredient_dinosaur.get_price.return_value = 500
        assert burger.get_price() == 1933

    def test_get_receipt(self, burger, mock_red_bun, mock_ingredient_sour_cream, mock_ingredient_dinosaur):
        burger.bun = mock_red_bun
        burger.ingredients = [mock_ingredient_sour_cream, mock_ingredient_dinosaur]
        mock_red_bun.get_name.return_value = 'red bun'
        mock_red_bun.get_price.return_value = 666
        mock_ingredient_sour_cream.get_name.return_value = 'sour cream'
        mock_ingredient_sour_cream.get_type.return_value = 'SAUCE'
        mock_ingredient_sour_cream.get_price.return_value = 101
        mock_ingredient_dinosaur.get_name.return_value = 'dinosaur'
        mock_ingredient_dinosaur.get_type.return_value = 'FILLING'
        mock_ingredient_dinosaur.get_price.return_value = 500
        expected_receipt = (
            "(==== red bun ====)\n"
            "= sauce sour cream =\n"
            "= filling dinosaur =\n"
            "(==== red bun ====)\n"
            "\n"
            f"Price: {burger.get_price()}"
        )
        assert burger.get_receipt() == expected_receipt
