products = {}

while True:
    print("\n==== inventory management ====")
    print("1. add product")
    print("2. show product")
    print("3. search product")
    print("4. update product")
    print("5. sell product")
    print("6. total inventory value")
    print("7. exit")

    choice = input("enter your choice:")

    if choice == "1":

        name = input("enter product name: ").lower()

        if name in products:
            print("product name already exists")

        else:
            price = float(input("enter the price:"))
            quantity = int(input("enter the quantity:"))

            if price <= 0 or quantity <= 0:
                print("price or quantity should be greater than 0")

            else:
                products[name] = {
                    "price" : price,
                    "quantity" : quantity
                }
                print("product added successfully")

    elif choice == "2":
        if len(products) == 0:
            print("no products")

        else:

            print("\n=== product details ===")

            for name, details in products.items():
                print("product name:",name.title())
                print("price:",details["price"])
                print("quantity:",details["quantity"])

    elif choice == "3":
        name = input("enter product name to search:").lower()

        if name in products:

            print("product name:",name.title())
            print("price:",products[name]["price"])
            print("quantity:",products[name]["quantity"])

        else:
            print("product not found")

    elif choice == "4":
        name = input("enter product name to update:").lower()

        if name in products:

            price = float(input("enter new price:"))
            quantity = int(input("enter new quantity"))

            if price <= 0 or quantity <= 0:
                print("price or quantity should be greater than 0")

            else:
               products[name]["price"] = price
               products[name]["quantity"] = quantity
               
               print("product updated successfully")

        else:
            print("product not found")

    elif choice == "5":
        name = input("enter product name to sell:").lower()

        if name in products:
            sell_quantity = int(input("enter sell quantity"))

            if sell_quantity <= 0:
                print("sell quantity should be greater than 0")

            elif sell_quantity <= products[name]["quantity"]:
                products[name]["quantity"] -= sell_quantity

                amount = sell_quantity * products[name]["price"]

                print("product sold successfully")
                print("total bill:",amount)
                print("remaining quantity:",products[name]["quantity"])

            else:
                print("insufficient stock")

        else:
            print("product not found")

    elif choice == "6":

        total_value = 0

        for details in products.values():

            total_value += details["price"] * details["quantity"]

        print("total inventory:",total_value)

    elif choice == "7":
        print("thank you for using our app")
        break

    else:
        print("invalid choice") 