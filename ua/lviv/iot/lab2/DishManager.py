from ua.lviv.iot.lab2.Dish import Dish
from typing import List


class DishManager():
    dishes_list = List

    def search_by_menu(self, type_of_menu):
        parameter_list = []
        for dish in self.dishes_list:
            if type_of_menu == dish.type_of_menu:
                parameter_list.append(dish)
        return parameter_list

    def sort_by_calories(self):
        self.dishes_list.sort(key=lambda dish: dish.caloric_content)
        return self.dishes_list

    def print_list(self, dishes_list):
        for dish in dishes_list:
            print(dish)
