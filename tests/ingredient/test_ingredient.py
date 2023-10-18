from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


def test_ingredient():
    # criando insâncias/objetos
    ingred_01 = Ingredient("salmão")
    ingred_02 = Ingredient("ovo")
    ingred_03 = Ingredient("farinha")
    ingred_04 = Ingredient("salmão")

    # testando nomes e restrições
    assert ingred_01.name == "salmão"
    assert ingred_01.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
    assert ingred_02.name == "ovo"
    assert ingred_02.restrictions == {Restriction.ANIMAL_DERIVED}
    assert ingred_03.name == "farinha"
    assert ingred_03.restrictions == {Restriction.GLUTEN}

    # testando __eq__
    assert ingred_01.__eq__(ingred_02) is False
    assert ingred_01.__eq__(ingred_03) is False
    assert ingred_02.__eq__(ingred_03) is False
    assert ingred_01.__eq__(ingred_04) is True

    # testando repr
    assert repr(ingred_01) == "Ingredient('salmão')"
    assert repr(ingred_02) == "Ingredient('ovo')"
    assert repr(ingred_03) == "Ingredient('farinha')"
    assert repr(ingred_04) == "Ingredient('salmão')"

    # testando hash
    assert hash(ingred_01) != hash(ingred_02)
    assert hash(ingred_01) == hash(ingred_04)
    assert hash(ingred_02) != hash(ingred_03)
