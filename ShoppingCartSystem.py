cart = []
while True:
    try:
        productQuantity = int(input("Please enter how many products you want to add: "))
        if productQuantity >= 0:
            break
        else:
            print("Please enter a number equal or bigger than zero.")
    except ValueError:
        print("You have to enter an integer.")