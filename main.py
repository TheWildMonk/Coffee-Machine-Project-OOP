# Importing object libraries
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

main_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

close_machine = False
while not close_machine:
    user_choice = input(f"What would you like? ({main_menu.get_items()}): ")
    if user_choice == "off":
        close_machine = True
    elif user_choice == "report":
        f"{coffee_maker.report()}\n{money_machine.report()}"
    elif main_menu.find_drink(user_choice) is None:
        ""
    else:
        user_choice = main_menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(user_choice):
            if money_machine.make_payment(user_choice.cost):
                coffee_maker.make_coffee(user_choice)
