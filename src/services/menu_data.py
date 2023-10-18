import csv
from typing import Set
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes: Set[Dish] = set()
        self._load_data()

    def _load_data(self):
        new_dish = {}
        with open(self.source_path, newline="", encoding="utf-8") as csvfile:
            reader_to_Dict = csv.DictReader(csvfile)
            for row in reader_to_Dict:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                ingredient = Ingredient(ingredient_name)

                if dish_name not in new_dish:
                    new_dish[dish_name] = Dish(dish_name, dish_price)

                # add os ingredientes de cada linha do arqv.
                new_dish[dish_name].add_ingredient_dependency(
                    ingredient, recipe_amount
                )

        self.dishes = set(new_dish.values())
