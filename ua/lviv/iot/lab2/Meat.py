from ua.lviv.iot.lab2.Dish import Dish

from ua.lviv.iot.lab2.DishType import DishType


class Meat(Dish):
    def __init__(self, caloric_content, dish_name, price, id, time_to_cock):
        super(Meat, self).__init__(caloric_content, dish_name, price, id)
        self.time_to_cock = time_to_cock
        self.DishType = DishType.meat

    def __str__(self):
        return super(Meat, self).__str__() + " Time to cock: " + str(self.time_to_cock)
