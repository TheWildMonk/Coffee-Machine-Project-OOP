# Importing object libraries
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Object declaration
main_menu = Menu()
coffee_machine = CoffeeMaker()
process_money = MoneyMachine()

close_machine = False
while not close_machine:
    user_choice = input(f"What would you want? ({main_menu.get_items()}): ")
    if user_choice == "off":
        close_machine = True
    elif user_choice == "report":
        f"{coffee_machine.report()}\n{process_money.report()}"
    else:
        coffee = main_menu.find_drink(user_choice)
        if coffee is not None and coffee_machine.is_resource_sufficient(coffee):
            payment = process_money.make_payment(coffee.cost)
            if payment:
                coffee_machine.make_coffee(coffee)