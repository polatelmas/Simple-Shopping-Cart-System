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

print("Enter the informations about product")
for i in range(productQuantity):
    print(f"\n{i+1}. Product:")

    productName = input("Product Name: ")

    while True:
        try:
            productPrice = float(input("Price for one in Turkish Lira (TL): "))
            productQuantity = int(input("Quantity (Amount): "))
            if productPrice < 0 or productQuantity < 0:
                print("Price and Quantity cannot be negative. Please enter again.")
            else:
                break
        except ValueError:
            print("Please enter float for price and integer for quantity.")

    product = {
        "Name": productName,
        "Price": productPrice,
        "Quantity": productQuantity
    }
    cart.append(product)

print("Total Cart and Calculations")
for item in cart:
    productTotal = item["price"] * item["quantity"]
    print(f"{item["name"]} ({item["quantity"]} quantity x {item["price"]:.2f} TL): {productTotal:.2f} TL")
    sumOfTotalPrice += productTotal

print(f"\Cart Subtotal: {sumOfTotalPrice:.2f} TL")