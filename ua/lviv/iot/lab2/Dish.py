from abc import ABC


class Dish(ABC):
    type_of_menu = "None"

    def __init__(self, caloric_content, dish_name, price, id):
        self.id = id
        self.price = price
        self.dish_name = dish_name
        self.caloric_content = caloric_content

    def __str__(self):
        return str(self.DishType) + " " + str(self.id) + " " + str(self.price) + " " + str(
            self.dish_name) + " " + str(self.caloric_content) + " "
