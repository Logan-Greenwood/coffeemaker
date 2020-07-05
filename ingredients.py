# ingredients in machine
water_in_machine = int(input("ml of water available: "))
milk_in_machine = int(input("ml of milk available: "))
beans_in_machine = int(input("grams of beans available: "))

cups_available = min(water_in_machine // 200, milk_in_machine // 50, beans_in_machine // 15)
print(cups_available)


# ingredients needed
cups_to_make = int(input("Enter number of cups to be made: "))
#print(cups_to_make, " cups")

water_required = 200 * cups_to_make
milk_required = 50 * cups_to_make
beans_required = 15 * cups_to_make

# print("water required:", water_required, "m")
# rint("milk required:", milk_required, "ml")
# print("beans required", beans_required, "g")

if cups_available > cups_to_make:
    print("Yes, I can make that amount of coffee", cups_available - cups_to_make, "(and even N more than that)")
elif cups_available == cups_to_make:
    print("Yes, I can make that amount of coffee")
else:
    print("No, I can make only", cups_available, "cups of coffee")