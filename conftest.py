import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.database import Database

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def mock_red_bun():
    mock_bun = Mock()
    mock_bun.name = 'red bun'
    mock_bun.price = 666
    return mock_bun

@pytest.fixture
def mock_ingredient_sour_cream():
    mock_ingredient = Mock()
    mock_ingredient.type = 'SAUCE'
    mock_ingredient.name = 'sour cream'
    mock_ingredient.price = 101
    return mock_ingredient

@pytest.fixture
def mock_ingredient_dinosaur():
    mock_ingredient = Mock()
    mock_ingredient.type = 'FILLING'
    mock_ingredient.name = 'dinosaur'
    mock_ingredient.price = 500
    return mock_ingredient

@pytest.fixture
def database():
    database = Database()
    return database