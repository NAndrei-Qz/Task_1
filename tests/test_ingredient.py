from praktikum.ingredient import Ingredient
import pytest


class TestIngredient:
    @pytest.mark.parametrize(
        'ingredient_type, ingredient_name, ingredient_price',
        [
            ('SAUCE', 'cheesy', 88),
            ('', 'cheesy', 88),
            (None, 'cheesy', 88),
            (999, 'cheesy', 88)
        ]
    )
    def test_get_ingredient_type(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize(
        'ingredient_type, ingredient_name, ingredient_price',
        [
            ('FILLING', 'Horsemeat', 777),
            ('FILLING', '', 777),
            ('FILLING', None, 777),
            ('FILLING', 0, 777)
        ]
    )
    def test_get_ingredient_name(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_name() == ingredient_name
    
    @pytest.mark.parametrize(
        'ingredient_type, ingredient_name, ingredient_price',
        [
            ('FILLING', 'Horsemeat', 777),
            ('FILLING', 'Horsemeat', -777),
            ('FILLING', 'Horsemeat', 77.7),
            ('FILLING', 'Horsemeat', '777')
        ]
    )
    def test_get_ingredient_price(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_price() == ingredient_price