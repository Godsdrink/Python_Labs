from ua.lviv.iot.lab2.Desert import Desert
from ua.lviv.iot.lab2.Meat import Meat
from ua.lviv.iot.lab2.Soup import Soup
from ua.lviv.iot.lab2.SideDish import SideDish
from ua.lviv.iot.lab2.DishManager import DishManager

if __name__ == '__main__':
    desert = Desert(123.2, "Sladkaia kuchka", 15, 1, 500)
    meat = Meat(50.5, "Miasnaia kuchka", 15, 2, 20)
    side_dish = SideDish(141241.2, "Side dish", 5, 3, 5)
    soup = Soup(50, "Soup", 20, 4, 100)
    manager = DishManager()
    manager.dishes_list = [desert, meat, side_dish, soup]
    manager.print_list(manager.dishes_list)
    print("\n")
    manager.print_list(manager.search_by_menu("Soup"))
    print("\n")
    manager.print_list(manager.sort_by_calories())
