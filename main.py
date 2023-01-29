# import transaction module
from transaction import Transaction

# defined menu function to show all menu of Super Cashier system.
def menu():
    """
    This function contains menu of Super Cashier system.
    """
    
    # create object of Transaction
    transaction = Transaction()
    
    # run this code if all input are valid
    try:
        
        # print main menu
        while True:
            print("")
            print(" "*15, "Menu", " "*15)
            print("="*36)
            print("1. Add item to the shopping list")
            print("2. Update item in the shopping list")
            print("3. Delete item in the shopping list")
            print("4. Check the shopping list")
            print("5. Reset the shopping list")
            print("6. Total price")
            print("7. Check out")
            print("8. History of transactions")
            print("9. Exit")

            print("")
            choice = int(input("Menu choice: "))

            if choice == 1:
                transaction.add_item()
            elif choice == 2:

                # print menu to update item name, item quantity, and item price
                while True:
                    print("")
                    print(" "*15, "Menu", " "*15)
                    print("="*36)
                    print("1. Update item name")
                    print("2. Update item quantity")
                    print("3. Update item price")
                    print("4. Back to main menu")

                    print("")
                    choice_2 = int(input("Menu choice: "))

                    if choice_2 == 1:
                        transaction.update_item_name()
                    elif choice_2 == 2:
                        transaction.update_item_qty()
                    elif choice_2 == 3:
                        transaction.update_item_price()
                    elif choice_2 == 4:
                        break
                    else:
                        print("Incorrect choice")

            elif choice == 3:
                transaction.delete_item()
            elif choice == 4:
                transaction.check_order()
            elif choice == 5:
                
                # this is check-out confirmation
                while True:
                    print("")
                    print("Are you sure want to reset the shopping list? All items will be deleted from the shopping list")
                    print("1. Yes")
                    print("2. No")

                    print("")
                    choice_3 = int(input("Menu choice: "))
                    print("")

                    if choice_3 == 1:
                        transaction.reset_item()
                        break
                    elif choice_3 == 2:
                        break
                    else:
                        print("Incorrect choice")
                                      
            elif choice == 6:
                transaction.show_total()
                
            elif choice == 7:
                
                while True:
                    print("")
                    print("Are you sure want to check out all items in the shopping list?")
                    print("1. Yes")
                    print("2. No")

                    print("")
                    choice_4 = int(input("Menu choice: "))
                    print("")

                    if choice_4 == 1:
                        transaction.check_out()
                        break
                    elif choice_4 == 2:
                        break
                    else:
                        print("Incorrect choice")
                        
            elif choice == 8:
                transaction.history_transaction()
                    
            elif choice == 9:

                # create exit confirmation
                while True:
                    print("")
                    print("Are you sure want to exit? All items in the current shopping list will be deleted.")
                    print("1. Yes")
                    print("2. No")

                    print("")
                    choice_5 = int(input("Menu choice: "))

                    if choice_5 == 1:
                        transaction.reset_item()
                        return
                    elif choice_5 == 2:
                        break
                    else:
                        print("Incorrect choice")

            else:
                print("Incorrect choice")
    
    # run this code if the input is invalid
    except ValueError:
        print("")
        print("Incorrect input")
        menu()


menu()