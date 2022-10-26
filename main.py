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

money = 0.0

def MakeEspresso():
    """Makes espresso"""
    water = MENU["espresso"]["ingredients"]["water"]
    coffee = MENU["espresso"]["ingredients"]["coffee"]
    cost = MENU["espresso"]["cost"]

    # Checking resources for necessary ingredients
    if resources["water"] < 50:
        return "Sorry, there isn't enough water."
    elif resources["coffee"] < 18:
        return "Sorry, there isn't enough coffee."

    # Subtracting the order from the resources available
    resources["water"] -= water
    resources["coffee"] -= coffee

    # returns an update to money for the price of the drink made, as well as a statement saying thank you for ordering.
    function_return = [(money + cost), "Here's your espresso ☕️. Enjoy!"]
    return function_return

def MakeLatte():
    """Makes latte"""
    water = MENU["latte"]["ingredients"]["water"]
    milk = MENU["latte"]["ingredients"]["milk"]
    coffee = MENU["latte"]["ingredients"]["coffee"]
    cost = MENU["latte"]["cost"]

    # Checking resources for necessary ingredients
    if resources["water"] < 200:
        return "Sorry, there isn't enough water."
    elif resources["milk"] < 150:
        return "Sorry, there isn't enough milk."
    elif resources["coffee"] < 24:
        return "Sorry, there isn't enough coffee."

    # Subtracting the order from the resources available
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee

    # returns an update to money for the price of the drink made, as well as a statement saying thank you for ordering.
    function_return = [(money + cost), "Here's your latte ☕️. Enjoy!"]
    return function_return

def MakeCappuccino():
    """Makes cappuccino"""
    water = MENU["cappuccino"]["ingredients"]["water"]
    milk = MENU["cappuccino"]["ingredients"]["milk"]
    coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    cost = MENU["cappuccino"]["cost"]

    # Checking resources for necessary ingredients
    if resources["water"] < 250:
        return "Sorry, there isn't enough water."
    elif resources["milk"] < 100:
        return "Sorry, there isn't enough milk."
    elif resources["coffee"] < 24:
        return "Sorry, there isn't enough coffee."

    # Subtracting the order from the resources available
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee

    # returns an update to money for the price of the drink made, as well as a statement saying thank you for ordering.
    function_return = [(money + cost), "Here's your cappuccino ☕️. Enjoy!"]
    return function_return


def CheckResources():
    """Tells users a summary of the current resource values"""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money}')



on_off = ''
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}
user_coins = {}
while on_off != 'off':
    # get user choice of drink
    user_choice = input('\tWhat drink would you like? (espresso/latte/cappuccino): ')
    if user_choice != "report" and user_choice != "off":
        # test: not accepting user coins if the resource for their chosen drink are not enough
        if user_choice == 'espresso':
            if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
                user_choice = ""
                print("Sorry, there isn't enough water for your espresso.")
            elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
                user_choice = ""
                print("Sorry, there isn't enough coffee for your espresso")
            else:
                # get the amount of coins user wants pay with
                print("Please insert coins.")
                user_coins = {
                    "quarters": int(input("how many quarters?: ")) * coins["quarters"],
                    "dimes": int(input("how many dimes?: ")) * coins["dimes"],
                    "nickles": int(input("how many nickles?: ")) * coins["nickles"],
                    "pennies": int(input("how many pennies?: ")) * coins["pennies"]
                }
        elif user_choice == 'latte':
            if resources["water"] < MENU["latte"]["ingredients"]["water"]:
                user_choice = ""
                print("Sorry, there isn't enough water for your latte.")
            elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
                user_choice = ""
                print("Sorry, there isn't enough milk for your latte.")
            elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
                user_choice = ""
                print("Sorry, there isn't enough coffee for your latte.")
            else:
                # get the amount of coins user wants pay with
                print("Please insert coins.")
                user_coins = {
                    "quarters": int(input("how many quarters?: ")) * coins["quarters"],
                    "dimes": int(input("how many dimes?: ")) * coins["dimes"],
                    "nickles": int(input("how many nickles?: ")) * coins["nickles"],
                    "pennies": int(input("how many pennies?: ")) * coins["pennies"]
                }
        elif user_choice == "cappuccino":
            if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
                user_choice = ""
                print("Sorry, there isn't enough water for your cappuccino.")
            elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
                user_choice = ""
                print("Sorry, there isn't enough milk for your cappuccino.")
            elif resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
                user_choice = ""
                print("Sorry, there isn't enough water for your cappuccino.")
            else:
                # get the amount of coins user wants pay with
                print("Please insert coins.")
                user_coins = {
                    "quarters": int(input("how many quarters?: ")) * coins["quarters"],
                    "dimes": int(input("how many dimes?: ")) * coins["dimes"],
                    "nickles": int(input("how many nickles?: ")) * coins["nickles"],
                    "pennies": int(input("how many pennies?: ")) * coins["pennies"]
                }

    # summing up the total of coins given by the user
    user_coin_total = sum(user_coins.values())
    user_refund = 0.0
    if user_choice == "espresso":
        if user_coin_total > MENU["espresso"]["cost"]:
            user_refund = user_coin_total - MENU["espresso"]["cost"]
            print(f"Your refund: ${round(user_refund, 2)}")
    elif user_choice == "latte":
        if user_coin_total > MENU["latte"]["cost"]:
            user_refund = user_coin_total - MENU["latte"]["cost"]
            print(f"Your refund: ${round(user_refund, 2)}")
    elif user_choice == "cappuccino":
        if user_coin_total > MENU["cappuccino"]["cost"]:
            user_refund = user_coin_total - MENU["cappuccino"]["cost"]
            print(f"Your refund: ${round(user_refund, 2)}")

    # print(f"Your refund: ${round(user_refund, 2)}")

    if user_choice == 'report':
        CheckResources()
    elif user_choice == 'espresso':
        # Determines whether user can even make the purchase of this drink. the condition here would need to sum up all the coins before determining whether the user's coins are less than the drink cost.
        if user_coin_total < MENU["espresso"]["cost"]:
            print("Sorry, the money you gave isn't enough. Money refunded. ")
            # giving the user back their money by setting all the user coins to zero
            user_coins = {coins: 0 for coins in user_coins}
            # test: seeing if all values in user_coins got set back to 0.
            # print(user_coins)
        # capture necessary return values from the MakeEspresso function without having to do multiple calls to it, reducing the amount of times resources get changed.
        else:
            espresso = MakeEspresso()
            money = espresso[0]
            print(espresso[1])
    elif user_choice == 'latte':
        # Determines whether user can even make the purchase of a latte. the condition here would need to sum up all the coins before determining whether the user's coins are less than the drink cost.
        if user_coin_total < MENU["latte"]["cost"]:
            print("Sorry, the money you gave isn't enough. Money refunded. ")
            # giving the user back their money by setting all the user coins to zero
            user_coins = {coins: 0 for coins in user_coins}
        # capture necessary return values from the MakeLatte function without having to do multiple calls to it, reducing the amount of times resources get changed.
        else:
            latte = MakeLatte()
            money = latte[0]
            print(latte[1])
    elif user_choice == 'cappuccino':
        # Determines whether user can even make the purchase of a cappuccino. the condition here would need to sum up all the coins before determining whether the user's coins are less than the drink cost.
        if user_coin_total < MENU["cappuccino"]["cost"]:
            print("Sorry, the money you gave isn't enough. Money refunded. ")
            # giving the user back their money by setting all the user coins to zero
            user_coins = {coins: 0 for coins in user_coins}
        # capture necessary return values from the MakeLatte function without having to do multiple calls to it, reducing the amount of times resources get changed.
        else:
            cappuccino = MakeCappuccino()
            money = cappuccino[0]
            print(cappuccino[1])

    on_off = user_choice
