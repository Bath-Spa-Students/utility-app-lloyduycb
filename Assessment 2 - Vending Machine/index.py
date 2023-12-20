from time import sleep

menu = {
    'A1': {'item': 'Shani', 'price': 1.50, 'stock': 10},
    'A2': {'item': 'Chips Oman', 'price': 1.00, 'stock': 15},
    'A3': {'item': 'Sohar Chips', 'price': 1.00, 'stock': 15},
    'B1': {'item': 'Mai Dubai', 'price': 1.00, 'stock': 12},
    'B2': {'item': 'Zoom Candy', 'price': 0.75, 'stock': 20},
    'B3': {'item': 'Pepsi', 'price': 2.50, 'stock': 20},
    'C1': {'item': 'Mountain Dew', 'price': 2.50, 'stock': 20}
}

def display_menu():
    ascii_art = r'''
    ,--.   ,--.                ,--.,--.                   ,--.   ,--.              ,--.     ,--.
     \  `.'  /,---. ,--,--,  ,-|  |`--',--,--,  ,---.     |   `.'   | ,--,--. ,---.|  ,---. `--',--,--,  ,---.
      \     /| .-. :|      \' .-. |,--.|      \| .-. |    |  |'.'|  |' ,-.  || .--'|  .-.  |,--.|      \| .-. :
       \   / \   --.|  ||  |\ `-' ||  ||  ||  |' '-' '    |  |   |  |\ '-'  |\ `--.|  | |  ||  ||  ||  |\   --.
        `-'   `----'`--''--' `---' `--'`--''--'.`-  /     `--'   `--' `--`--' `---'`--' `--'`--'`--''--' `----'
                                               `---'
    '''
    print(ascii_art)
    print("Vending Machine Menu:")
    for code, item_info in menu.items():
        print(
            f"{code}: {item_info['item']} - AED {item_info['price']} ({item_info['stock']} in stock)")
        
purchase_made = False # Flag to track purchases
money_entered = False # Flag to track whether money has been entered
first_purchase = True # Flag to check the first purchase

while True:
    display_menu()

    while True:
        code = input("What do you want to buy? Enter code: ").upper()
        if code in menu and menu[code]['stock'] > 0:
            item = menu[code]
            break
        elif code not in menu:
            print("Invalid Code")
        else:
            print("Sorry, this item is out of stock.")
    
    if not purchase_made:  # Only ask for money if a purchase hasn't been made yet
        while True:
            if not money_entered:  # Only ask for money if it hasn't been entered yet
                try:
                    money = int(input("Insert money inside me. "))
                    if money > 0:
                        print(f"You have: AED {money}")
                        money_entered = True  # Set the flag to indicate money has been entered
                    else:
                        print("Invalid input. Enter a valid positive integer.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")


            if money_entered and money >= item['price']:
                change = money - item['price']
                print(f"{item['item']} is getting dispensed.")
                print(f"Your change is {change}")  # Display the change
                item['stock'] -= 1  # Update stock after purchase
                money = change
                purchase_made = True  # Set the flag to indicate a purchase has been made
                money_entered = False  # Reset the money flag for the next purchase
                break
            elif money_entered:
                print("Insufficient funds.")

    money_entered = False  # Reset the money flag for the next purchase
    
    if input("Would you like to buy another item? y/n ").lower() == "y": # or "Y"
        pass
    else:
        print("Thank you for shopping with Lloyd2Go, See you next time!")
        sleep(2)
        break



