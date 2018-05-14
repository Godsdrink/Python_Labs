from ua.lviv.iot.lab2.Dish import Dish

from ua.lviv.iot.lab2.DishType import DishType


class Soup(Dish):
    def __init__(self, caloric_content, dish_name, price, id, ingridients):
        super(Soup, self).__init__(caloric_content, dish_name, price, id)
        self.ingridients = ingridients
        self.DishType = DishType.soup

    def __str__(self):
        return super(Soup, self).__str__() + " ingridients: " + str(self.ingridients)
