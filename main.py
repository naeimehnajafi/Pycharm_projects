# Day 15 python bootcamp
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
    # TODO 1. Prompt the user for input
    choice = input(" What would you like? (espresso/latte/cappuccino): ")

    # Check the user's input
    if choice == "off":
        # TODO 2.Turn off the machine
        print("Turning off the machine...")
        break
    elif choice == "report":
        # TODO 3. Print the report
        # multi line editing: press down option+shift and choose multiple line.
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif choice in MENU:
        # TODO 4. Check if there are enough resources to make the drink
        if all(resources[resource] >= MENU[choice]['ingredients'][resource] for resource in
               MENU[choice]['ingredients']):
            # Prompt the user to insert coins
            print("Please insert coins.")
            quarters_num = input("how many quarters?: ")
            dimes_num = input("how many dimes?: ")
            nickels_num = input("how many nickles?: ")
            pennies_num = input("how many pennies?: ")

            # TODO 5. Calculate the monetary value of the coins inserted
            coin_values = {
                'quarters': 0.25,
                'dimes': 0.10,
                'nickels': 0.05,
                'pennies': 0.01,
            }
            # Calculate the total value of the coins
            total_value = sum(int(coin_num) * coin_values[coin_type] for coin_type, coin_num in
                              {'quarters': quarters_num, 'dimes': dimes_num, 'nickels': nickels_num,
                               'pennies': pennies_num}.items())
            # TODO 6: check transaction successful
            if total_value >= MENU[choice]['cost']:
                # Calculate the change
                change = total_value - MENU[choice]['cost']

                # TODO 7. update the resources
                for resource, quantity in MENU[choice]['ingredients'].items():
                    resources[resource] -= quantity

                # Add the cost of the drink to the total money collected
                money += MENU[choice]['cost']

                # Print the change
                print(f"Change: ${change:.2f}")
                print(f"Here is your {choice} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            # TODO 4. Print an error message if there are not enough resources to make the drink
            missing_resources = []
            for resource, quantity in MENU[choice]['ingredients'].items():
                if resources[resource] < quantity:
                    missing_resources.append(resource)
            print(f"Sorry, we don't have enough {' and '.join(missing_resources)} to make a {choice}.")
    else:
        # Invalid choice
        print("Invalid choice. Please try again.")
