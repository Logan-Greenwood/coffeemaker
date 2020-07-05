def coffee_operation():
    water_in_machine = 400
    milk_in_machine = 540
    beans_in_machine = 120
    money_in_machine = 550
    disposable_cups_in_machine = 9

    print(
"The coffee machine has:\n%s of water\n%s of milk\n%s of \
coffee beans\n%s of disposable cups\n%s of money"
%(water_in_machine, milk_in_machine, beans_in_machine, disposable_cups_in_machine,
money_in_machine))


    buy_fill_take = input("Write action (buy, fill, take): ")
    if buy_fill_take == "buy":
        what_drink = input("What do you want to buy? 1\ - espresso, 2 - latte, 3 - cappuccino: ")
        if what_drink == "1":
            water_in_machine -= 250
            milk_in_machine -= 0
            beans_in_machine -= 16
            money_in_machine += 4
            disposable_cups_in_machine -= 1
            return (
"The coffee machine has:\n%s of water\n%s of milk\n%s of \
coffee beans\n%s of disposable cups\n%s of money"
%(water_in_machine, milk_in_machine, beans_in_machine, disposable_cups_in_machine,
money_in_machine))

        elif what_drink == "2":
            water_in_machine -= 350
            milk_in_machine -= 75
            beans_in_machine -= 20
            money_in_machine += 7
            disposable_cups_in_machine -= 1
            return (
"The coffee machine has:\n%s of water\n%s of milk\n%s of \
coffee beans\n%s of disposable cups\n%s of money"
% (water_in_machine, milk_in_machine, beans_in_machine, disposable_cups_in_machine,
money_in_machine))

        elif what_drink == "3":
            water_in_machine -= 200
            milk_in_machine -= 100
            beans_in_machine -= 12
            money_in_machine += 6
            disposable_cups_in_machine -= 1
            return (
"The coffee machine has:\n%s of water\n%s of milk\n%s of \
coffee beans\n%s of disposable cups\n%s of money"
% (water_in_machine, milk_in_machine, beans_in_machine, disposable_cups_in_machine,
money_in_machine))
    elif buy_fill_take == "fill":
        water_in_machine += int(input("Water to add: "))
        milk_in_machine += int(input("Milk to add: "))
        beans_in_machine += int(input("Beans to add: "))
        disposable_cups_in_machine += int(input("Cups to add: "))
        return (
"The coffee machine has:\n%s of water\n%s of milk\n%s of \
coffee beans\n%s of disposable cups\n%s of money"
% (water_in_machine, milk_in_machine, beans_in_machine, disposable_cups_in_machine,
money_in_machine))

    elif buy_fill_take == "take":
        print("I gave you $", money_in_machine)
        print("")
        money_in_machine -= money_in_machine
        return (
"The coffee machine has:\n%s of water\n%s of milk\n%s of \
coffee beans\n%s of disposable cups\n%s of money"
% (water_in_machine, milk_in_machine, beans_in_machine, disposable_cups_in_machine,
money_in_machine))

print(coffee_operation())