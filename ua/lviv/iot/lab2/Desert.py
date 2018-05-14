from ua.lviv.iot.lab2.Dish import Dish

from ua.lviv.iot.lab2.DishType import DishType


class Desert(Dish):
    def __init__(self, caloric_content, dish_name, price, id, sugar_content):
        super(Desert, self).__init__(caloric_content, dish_name, price, id)
        self.sugar_content = sugar_content
        self.DishType = DishType.desert

    def __str__(self):
        return super(Desert, self).__str__() + " Sugar content: " + str(self.sugar_content)
