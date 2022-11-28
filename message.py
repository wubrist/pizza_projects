def message():
 age = (int(input("pleas enter your age")))
 city = (input("do you live in Ber sheva?"))
 while age >= 18:
    print(age)
    print(city)
    sp = input("please enter size:")
    for size, price in size:
        sum += sp[size.index(size, price)]
        extra = input("do you want extras on your pizza?")
        quantity = int(input("how many pizzas do you want?"))
        if extra == "yes":
            sum += size[size.index(size, price)] + 2
        if city == "yes":
            sum += price[size.index(size, price)] + 20
        else:
            sum += price[size.index(size, price)] + 60

