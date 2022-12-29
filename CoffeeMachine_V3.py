# This version of the code is more compact because it removes unnecessary
# indentation levels and simplifies some logic. For example,
# the code uses a try-except block to handle invalid input when reading
# the coin counts, and it checks if all the necessary resources are available
# before prompting the user to insert coins, rather than checking the resources
# again after the coins have been inserted.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print("Turning off the machine...")
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif choice in MENU:
        if all(resources[resource] >= MENU[choice]['ingredients'][resource] for resource in
               MENU[choice]['ingredients']):
            print("Please insert coins.")
            quarters_num = input("how many quarters?: ")
            dimes_num = input("how many dimes?: ")
            nickels_num = input("how many nickels?: ")
            pennies_num = input("how many pennies?: ")

            coin_values = {
                'quarters': 0.25,
                'dimes': 0.10,
                'nickels': 0.05,
                'pennies': 0.01,
            }

            try:
                total_value = sum(int(coin_num) * coin_values[coin_type] for coin_type, coin_num in
                                  {'quarters': quarters_num, 'dimes': dimes_num, 'nickels': nickels_num,
                                   'pennies': pennies_num}.items())
            except ValueError:
                print("Invalid input. Please enter a valid positive integer for the coin counts.")
                continue

            if total_value >= MENU[choice]['cost']:
                change = total_value - MENU[choice]['cost']
                for resource, quantity in MENU[choice]['ingredients'].items():
                    resources[resource] -= quantity
                money += MENU[choice]['cost']
                print(f"Change: ${change:.2f}")
                print(f"Here is your {choice} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            missing_resources = []
            for resource, quantity in MENU[choice]['ingredients'].items():
                if resources[resource] < quantity:
                    missing_resources.append(resource)
            print(f"Sorry, we don't have enough {' and '.join(missing_resources)} to make a {choice}.")
    else:
        print("Invalid choice. Please try again.")
