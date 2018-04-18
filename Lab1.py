class Kitchen:
    amount = 0

    def __init__(self, dish_name="kuchka govnica", price=0, new_amount=0, quality="govno", caloric_content=0):
        self.dish_name = dish_name
        self.price = price
        self.new_amount = new_amount
        self.quality = quality
        self.caloric_content = caloric_content
        Kitchen.amount += new_amount

    def to_string(self):
        print("Name: " + self.dish_name + "; Price:", self.price,
              "; Amount:", self.new_amount, "; Quality:" + self.quality + "; Caloric content:", self.caloric_content,
              ";")

    def print_sum(self):
        print("Кількість " + self.dish_name + ": ", self.new_amount)

    @staticmethod
    def print_static_sum():
        print("Загальна кількість: ", Kitchen.amount)


if __name__ == '__main__':
    MiortvuiKot = Kitchen()
    CherstvuiHleb = Kitchen("Брожений хліб", 12.50, 2, "", 0)
    ocherednoiMusor = Kitchen("paket moloka", 20, 228, "mojno pit")

    print("\n")
MiortvuiKot.to_string()
CherstvuiHleb.to_string()
ocherednoiMusor.to_string()

print("\n")
MiortvuiKot.print_sum()
CherstvuiHleb.print_sum()
ocherednoiMusor.print_sum()

print("\n")
Kitchen.print_static_sum()
