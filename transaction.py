from tabulate import tabulate
from datetime import datetime


# defined a function to check is text a string and not a number or None
def check_string(text):
    """
    Parameters
    ==========
    text : str
            a tested text
            
    Returns
    ==========
    Invalid or None : str, NoneType
            validation wheter or not the text a string and not a number or None
    """
    
    if len(text) == 0 or len(text) == text.count(" "):
        return "Invalid"
    else:
        try:
            text = int(text)
            return "Invalid"
        except:
            pass


class Transaction:
    """
    A class to provides methods of transaction. The transaction will be processed and stored as shopping list.
    
    Methods
    ==========
    add_item :
            add item to the shopping list
            
    update_item_name :
            update item name in the shopping list
            
    update_item_quantity :
            update item quantity in the shopping list
            
    update_item_price :
            update item price in the shopping list
            
    delete_item :
            delete item in the shopping list
            
    reset_item :
            delete all items in the shopping list
            
    check_order :
            print the shopping list contains item name, item quantity, and item price
            
    total_price :
            calculate and print total price of all items in the shopping list and discount received
            
    check_out :
            check out all items in the shopping list and store the transaction on a table called history of transaction
            
    history_transaction :
            print history of transaction contains date and time of transaction and total price
    """
    
    # defined empty dictionary to store items
    shop_list = {}
    
    # defined empty list to store history of transaction
    hist_trans = []
    
    
    # defined method to add item to the shopping list
    def add_item(self):
        """
        A method to add item to the shopping list.
        
        Input
        ==========
        item name : str
                Item name must be string and not integer or None.
                If the input is integer or None, then the methods will ask to re-input the name.
        
        item quantity : int
                Item quantity must be integer and not string or None.
                If the input is string or None, then the methods will ask to re-input the quantity.
        
        item price : int, float
                Item price must be integer or float, not string or None.
                If the input is string or None, then the methods will ask to re-input the price.
        """
        
        while True:
            self.name = input("Item name: ")
        
            # create condition item name can't be empty or only contains space or a number
            if check_string(self.name) == "Invalid":
                print("Invalid input. Please input item name!")
            else:
                
                # create condition quantity is not a string
                try:
                    self.qty = int(input("Quantity: "))

                    # create condition quantity must be a non-negative number
                    if self.qty < 0:
                        print("Invalid input. Please input item quantity!")
                    else:
                        
                        # create condition price is not a string
                        try:
                            self.price = float(input("Price: "))

                            # create condition price must be a non-negative number
                            if self.price < 0:
                                print("Invalid input. Please input item price!")
                            else:
                                self.shop_list[self.name] = [self.qty, self.price]
                                print(f"{self.name} added to the shopping list")
                                break
                        except:
                            print("Invalid input. Please input item price!")
                except:
                    print("Invalid input. Please input item quantity!")
            
    
    # defined method to update item name in the shopping list
    def update_item_name(self):
        """
        A method to change item name in the shopping list.
        
        Input
        ==========
        old item name : str
                Item name must be in the shopping list.
                If the item name is not in the shopping list, then the input is invalid.
                
        new item name : str
                New item name must be string and not integer or None.
        """
        
        self.old_name = input("Previous item name: ")
        
        # create condition when the item name can't be found in the shopping list
        if self.old_name not in self.shop_list.keys():
            print(f"There's no {self.old_name} in the shopping list")
        else:
            while True:
                self.new_name = input("New item name: ")
                
                # create condition item name can't be empty or only contains space or a number
                if check_string(self.old_name) == "Invalid":
                    print("Invalid input. Please input item name!")
                else:
                    self.shop_list[self.new_name] = self.shop_list[self.old_name]
                    self.shop_list.pop(self.old_name)
                    print(f"{self.old_name} changed to {self.new_name}")
                    break
    
    
    # defined method to update item quantity in the shopping list
    def update_item_qty(self):
        """
        A method to change item quantity in the shopping list.
        
        Input
        ==========
        item name : str
                Item name must be in the shopping list.
                If the item name is not in the shopping list, then the input is invalid.
                
        new item quantity : str
                New item quantity must be integer and not string or None.
        """
        
        self.name = input("Item name: ")
        
        # create condition when the input can't be found in the shopping list
        if self.name not in self.shop_list.keys():
            print(f"There's no {self.name} in the shopping list")
        else:
            while True:
                try:
                    self.new_qty = int(input("New item quantity: "))
                    self.shop_list[self.name][0] = self.new_qty
                    print(f"{self.name} quantity updated")
                    break
                except:
                    print("Invalid input. Please input item quantity!")
    
    
    # defined method to update item price in the shopping list
    def update_item_price(self):
        """
        A method to change item price in the shopping list.
        
        Input
        ==========
        item name : str
                Item name must be in the shopping list.
                If the item name is not in the shopping list, then the input is invalid.
                
        new item price : str
                New item quantity must be integer or float, not string or None.
        """
        
        self.name = input("Item name: ")
        
        # create condition when the input can't be found in the shopping list
        if self.name not in self.shop_list.keys():
            print("There's no {self.name} in the shopping list")
        else:
            while True:
                try:
                    self.new_price = float(input("New item price: "))
                    self.shop_list[self.name][1] = self.new_price
                    print(f"{self.name} price updated")
                    break
                except:
                    print("Invalid input. Please input item price!")
    
    
    # defined method to delete an item in the shopping list
    def delete_item(self):
        """
        A method to delete item in the shopping list.
        
        Input
        ==========
        item name : str
                Item name must be in the shopping list.
                If the item name is not in the shopping list, then the input is invalid.
        """
        
        self.name = input("Item name: ")
        
        # create condition when the input can't be found in the shopping list
        if self.name not in self.shop_list.keys():
            print("There's no {self.name} in the shopping list")
        else:
            self.shop_list.pop(self.name)
            print(f"{self.name} is deleted from the shopping list")
    
    
    # defined method to delete all items in the shopping list
    def reset_item(self):
        """
        A method to delete all items in the shopping list.
        """
        
        self.shop_list.clear()
        print("All items are deleted from the shopping list.")
    
    
    # defined method to print all items in the shopping list
    def check_order(self):
        """
        A method to print all items in the shopping list as a tabular format.
        """
        
        print("\033[1m", "S H O P P I N G   L I S T", "\033[0m")
        
        # convert dictionary shop_list as tabular
        list_item = [(key, value[0], "{:,.2f}".format(value[1])) for key, value in self.shop_list.items()]  
        print(tabulate(list_item, headers = ["Name", "Quantity", "Price"], tablefmt="mixed_grid"))  
        
    
    # defined method to return total price
    def total_price(self):
        """
        A method to calcuate total price of all items in the shopping list.
        """
        
        # defined initial total price is 0
        self.total = 0
        
        # calculate total price of each item in the shopping list
        for item in self.shop_list.keys():
            self.total += self.shop_list[item][0] * self.shop_list[item][1]
        
        return self.total
    
    # defined method to return total discount
    def total_discount(self):
        """
        A method to calcuate discount received (if any).
        
        If total price more than Rp.500,000.00, then get 10% discount
        If total price more than Rp.300,000.00, then get 8% discount
        If total price more than Rp.200,000.00, then get 2% discount
        """

        # create condition when the customers get discount and calculate discount received
        if self.total > 500_000:
            self.disc = 0.1 * self.total
        elif self.total > 300_000:
            self.disc = 0.08 * self.total
        elif self.total > 200_000:
            self.disc = 0.02 * self.total
        else:
            self.disc = 0
        
        return self.disc


    # defined method to print total price and discount (if any)
    def show_total(self):
        """
        A method to print total price in the shopping list and discount received (if any).
        """
        
        self.total = self.total_price()
        self.disc = self.total_discount()

        # print total price before discount
        print(f"Total price : Rp. {self.total:,.2f}")

        # print discount received
        print(f"You get discount : Rp. {self.disc:,.2f}")

        # total price after discount
        print(f"Total price after discount : Rp. {self.total - self.disc:,.2f}") if self.disc > 0 else None
            
    
    # defined method to check out all items in the shopping list and store transaction in the history of transaction
    def check_out(self):
        """
        A method to check out all items in the shopping list.
        The transaction will be stored as history of transaction contains
        date and time of transaction, total price, discount received,
        and total price after discount.
        """
        
        self.total = self.total_price()
        self.disc = self.total_discount()

        # Store history of transaction in the list
        self.hist_trans.append([datetime.now().strftime("%Y %B %d %X"),
                                "{:,.2f}".format(self.total), 
                                "{:,.2f}".format(self.disc), 
                                "{:,.2f}".format(self.total - self.disc)])
        
        self.shop_list.clear()
        print("Check out succeed!")
    
    
    # defined method to print history of transaction
    def history_transaction(self):
        """
        A method to print history of transactions in tabular format
        contains date and time of transaction, total price, discount
        received, and total price after discount.
        """
        
        # convert and print list hist_trans as tabular
        print("\033[1m", "HISTORY OF TRANSACTIONS", "\033[0m")
        print(tabulate(self.hist_trans, headers = ["Date and Time Transaction",
                                                   "Total Price", 
                                                   "Discount",
                                                   "Total Price After Discount"], 
                       tablefmt="mixed_grid"))
    
    
    # defined method to cancel the transaction. All items in the shopping list will be reset.
    def cancel(self):
        """
        A method to cancel transaction and all items in the shopping list will be reset.
        """
        
        self.shop_list.clear()