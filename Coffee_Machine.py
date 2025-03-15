MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
machine = "ON"
global_water = 500
global_milk = 250
global_coffee = 100
global_profit = 0
total = 0
is_transaction_successful = True



def report():
    """Provides the report on resources available """
    print(f"Water : {global_water}")
    print(f"Milk : {global_milk}")
    print(f"Coffee : {global_coffee}")
    print(f"profit : {global_profit}")


def insert_money():
    """gets coins from customers and add them up"""
    global total
    total = int(input("insert dimes: ")) * 0.15
    total += int(input("insert quarter: ")) * 0.25
    total += int(input("insert pennies: ")) * 0.01
    total += int(input("insert nickel: ")) * 0.05
    return total


def calculate_money(total, cost):
    """"check if the inserted money is sufficient"""
    global global_profit
    if total == cost:
        global_profit += cost
        print(f"Enjoy you coffee and Here is the change {total}")
        return True
    elif total > cost:
        total -= cost
        global_profit += cost
        print(f"Enjoy you coffee and Here is the change {total}")
        return True
    else:
        money_needed = cost - total
        print(f"Insufficient Money, please insert {money_needed} more")
        return False

def deduct_resource (choice, is_transaction_successful):
    """Deducts resources only if the transaction is successful"""
    global global_water, global_milk, global_coffee
    if choice in MENU:
        price = MENU[choice]["cost"]
        ingredients = MENU[choice]["ingredients"]
        water = ingredients["water"]
        milk = ingredients["milk"]
        coffee = ingredients["coffee"]
        if water <= global_water and milk <= global_milk and coffee <= global_coffee and is_transaction_successful:
            global_water -= water
            global_milk -= milk
            global_coffee -= coffee
            return True
        else:
            return False

def calculate_resource(choice):
    """Calculates if the resource is sufficient to make the customer's choice"""
    global global_water, global_milk, global_coffee
    if choice in MENU:
        price = MENU[choice]["cost"]
        ingredients = MENU[choice]["ingredients"]
        water = ingredients["water"]
        milk = ingredients["milk"]
        coffee = ingredients["coffee"]
        print(f"remaining Water : {global_water}, remaining Milk : {global_milk},"
              f" remaining Coffee : {global_coffee}, Money_needed : {price}")

        if water <= global_water and milk <= global_milk and coffee <= global_coffee:
            print(f"Your {choice} is being prepared")
            return True
        else:
            if water >= global_water:
                print(f"Not enough Water to make {choice}")
            elif milk >= global_milk:
                print(f"Not enough milk to make {choice}")
            elif coffee >= global_coffee:
                print(f"Not enough Coffee to make {choice}")
            return False
    else:
        print("Type correct choice")


while machine != "OFF":
    choice = input("What would you like? (espresso/latte/cappuccino/report/OFF): ")
    if choice not in MENU and choice != "report" and choice != "OFF":
        print("Type correct choice")
    elif choice != "report" and choice != "OFF":
        if calculate_resource(choice):
            cost_price = MENU[choice]["cost"]
            is_transaction_successful = calculate_money(insert_money(),cost_price )
            deduct_resource(choice, is_transaction_successful)
        else:
            print("Sorry, Come after some Time!")
    elif choice == 'report':
        report()
    elif choice == "OFF":
        machine = "OFF"
        print("Machine is now OFF.")
