menu = [ "Pizza",  "Burger", "Pasta", "Fried Rice","Coffee"]
price = [250,150,180,200,801]

order = []
customer = ""
people = 0


def show_menu():
    print("========== MENU ==========")
    print("Food\t\tPrice")
    print("----------------------------------")
    for i in range(len(menu)):
        print(f"{menu[i]},₹{price[i]}")
    print("--------------------------")


def book_table():
    customer = input("Enter Customer Name: ")
    people = int(input("Enter Number of People: "))
    print("Table Booked Successfully")
    return customer, people


def food_order():
    while True:
        item = input("Enter Food Name: ").strip().lower()
        found = False
        for i in range(len(menu)):
            if item == menu[i].lower():
                quantity = int(input("Enter Quantity: "))
                amount = price[i] * quantity
                orders = {
                    "Item": menu[i],
                    "Quantity": quantity,
                    "Amount": amount
                }
                order.append(orders)
                print("Order Placed Successfully")
                found = True
                break
        if not found:
            print("Food Not Available")
        choice = input("Add More Item (yes/no): ").strip().lower()
        if choice != "yes":
            break


def bill(mjmcustomer, people):
    print("\n========== BILL ==========")
    print("Customer :", customer)
    print("People   :", people)
    print("-------------------------------")
    print("Item\t\tQty\tAmount")
    print("-------------------------------")

    total = 0

    for i in order:
        print(f"{i['Item']}\t\t{i['Quantity']}\t₹{i['Amount']}")
        total += i["Amount"]

    print("-------------------------------")
    print("Total Bill : ₹", total)
    print("Thank You! Visit Again.")


while True:

    print("\n===== RESTAURANT ORDER BOOKING =====")
    print("1. Show Menu")
    print("2. Book Table")
    print("3. Order Food")
    print("4. Print Bill")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        show_menu()

    elif choice == "2":
        customer, people = book_table()

    elif choice == "3":
        if customer == "":
            print("Please Book Table First.")
        else:
            show_menu()
            food_order()

    elif choice == "4":
        if customer == "":
            print("Please Book Table First.")
        elif len(order) == 0:
            print("Please Order Food First.")
        else:
            bill(customer, people)

    elif choice == "5":
        print("Closed.")
        break

    else:
        print("Invalid Choice")