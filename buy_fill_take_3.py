water_in_machine = 400
milk_in_machine = 540
beans_in_machine = 120
money_in_machine = 550
disposable_cups_in_machine = 9
ingredients = [water_in_machine, milk_in_machine, beans_in_machine, disposable_cups_in_machine]


buy_fill_take = ""

while buy_fill_take != "exit":

    buy_fill_take = input("Write action (buy, fill, take, remaining, exit):\n")

    if buy_fill_take == "buy":
        what_drink = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")

        if what_drink == "1":
            if water_in_machine > 250 and beans_in_machine > 16 and disposable_cups_in_machine > 1:

                water_in_machine -= 250
                milk_in_machine -= 0
                beans_in_machine -= 16
                money_in_machine += 4
                disposable_cups_in_machine -= 1
                print("I have enough resources, making you a coffee!\n")

            elif water_in_machine < 250:
                print("Sorry, not enough water!\n")
            elif beans_in_machine < 16:
                print("Sorry, not enough coffee!")
            elif disposable_cups_in_machine < 1:
                print("Sorry, not enough cups!")


        elif what_drink == "2":
            if water_in_machine > 350 and milk_in_machine > 75 and beans_in_machine > 20 and disposable_cups_in_machine > 1:
                water_in_machine -= 350
                milk_in_machine -= 75
                beans_in_machine -= 20
                money_in_machine += 7
                disposable_cups_in_machine -= 1
                print("I have enough resources, making you a coffee!\n")

            elif water_in_machine < 350:
                print("Sorry, not enough water!\n")
            elif milk_in_machine < 75:
                print("Sorry, not enough milk!")
            elif beans_in_machine < 20:
                print("Sorry, not enough coffee!")
            elif disposable_cups_in_machine < 1:
                print("Sorry, not enough cups!")




        elif what_drink == "3":
            if water_in_machine > 350 and milk_in_machine > 75 and beans_in_machine > 20 and disposable_cups_in_machine > 1:

                water_in_machine -= 200
                milk_in_machine -= 100
                beans_in_machine -= 12
                money_in_machine += 6
                disposable_cups_in_machine -= 1
                print("I have enough resources, making you a coffee!\n")

            elif water_in_machine < 200:
                print("Sorry, not enough water!\n")
            elif milk_in_machine < 100:
                print("Sorry, not enough milk!")
            elif beans_in_machine < 12:
                print("Sorry, not enough coffee!")
            elif disposable_cups_in_machine < 1:
                print("Sorry, not enough cups!")




    elif buy_fill_take == "fill":

        water_in_machine += int(input("Water to add:\n"))
        milk_in_machine += int(input("Milk to add:\n"))
        beans_in_machine += int(input("Beans to add:\n"))
        disposable_cups_in_machine += int(input("Cups to add:\n"))

    elif buy_fill_take == "take":
        print("I gave you $", money_in_machine)
        print("")
        money_in_machine -= money_in_machine

    elif buy_fill_take == "remaining":
        if water_in_machine < 0:
            water_in_machine = 0
        if milk_in_machine < 0:
            milk_in_machine = 0
        if beans_in_machine < 0:
            beans_in_machine = 0
        if disposable_cups_in_machine < 0:
            disposable_cups_in_machine = 0

        print(
"\nThe coffee machine has:\n%s of water\n%s of milk\n%s of \
coffee beans\n%s of disposable cups\n$%s of money\n"
% (water_in_machine, milk_in_machine, beans_in_machine, disposable_cups_in_machine,
money_in_machine))