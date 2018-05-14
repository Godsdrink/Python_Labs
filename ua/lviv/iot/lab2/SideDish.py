from ua.lviv.iot.lab2.Dish import Dish

from ua.lviv.iot.lab2.DishType import DishType


class SideDish(Dish):
    def __init__(self, caloric_content, dish_name, price, id, volume):
        super(SideDish, self).__init__(caloric_content, dish_name, price, id)
        self.volume = volume
        self.DishType = DishType.side_dish

    def __str__(self):
        return super(SideDish, self).__str__() + " Volume: " + str(self.volume)
