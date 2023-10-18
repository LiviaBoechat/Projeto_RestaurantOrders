from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import (
    Ingredient,
    Restriction,
)

# Req 2


def test_dish():
    # criando insâncias/objetos
    dish_01 = Dish("dish_01", 200.0)
    dish_02 = Dish("dish_02", 150.0)

    # testando atributos nome, preço
    assert dish_01.name == "dish_01"
    assert dish_01.price == 200.0
    assert dish_02.name == "dish_02"
    assert dish_02.price == 150.0

    # testando representação
    assert dish_01.__repr__() == "Dish('dish_01', R$200.00)"
    assert dish_02.__repr__() == "Dish('dish_02', R$150.00)"

    # testando equivalencia
    assert dish_01.__eq__(dish_01) is True
    assert dish_01.__eq__(dish_02) is False

    # testando hash
    assert hash(dish_01) == hash("Dish('dish_01', R$200.00)")
    assert hash(dish_01) != hash(dish_02)

    # testando adição de ingrediente
    dish_01.add_ingredient_dependency(Ingredient("ovo"), 5)
    dish_01.add_ingredient_dependency(Ingredient("salmão"), 1)

    # testando restrições com ingreddientes added
    assert dish_01.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }

    # testando lista ingredientes added e receita
    assert dish_01.get_ingredients() == {
        Ingredient("ovo"),
        Ingredient("salmão"),
    }
    assert dish_01.recipe == {Ingredient("ovo"): 5, Ingredient("salmão"): 1}

    # testando erros de tipagem de atributos
    with pytest.raises(ValueError) as error:
        Dish("ovo", -30)
    assert str(error.value) == "Dish price must be greater then zero."

    with pytest.raises(TypeError) as error:
        Dish("salmão", "480")
    assert str(error.value) == "Dish price must be float."
