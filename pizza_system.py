def pizza_system():
 size = ["s", "m", "l", "xl"]
 price = [40, 50, 60, 75]
 sum = 0
 age = int(input("pleas enter your age"))
 city = input("do you live in Ber sheva?")
 while age >= 18:
    sz = input("please enter size:")
    for sz in size:
        sum += price[size.index(sz)]
    extra = input("do you want extras on your pizza?")
    quantity = int(input("how many pizzas do you want?"))
    if extra == "yes":
        sum += price[size.index(sz)] + 2
    if city == "yes":
        sum += price[size.index(sz)] + 20
    else:
        sum += price[size.index(sz)] + 60
    con = input("Are yuo want to continue? y/n :")
    if con == "n":
        print("the total price will be: ", str(sum), "dollars")
        break

