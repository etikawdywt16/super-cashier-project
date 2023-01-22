from math import sqrt
from tabulate import tabulate

class Transaction:
    """This class defined functions of transactions."""
    
    # Defined empty dictionary to stored item as shopping list
    dict_item = {}
    
    # Defined function to add item to the shopping list
    def add_item(self):
        while True:
            self.name = input("Item name: ")
        
            # Make condition where name item can't be empty
            if len(self.name) == 0:
                print("Input item name!")
            else:
                
                # Make condition where quantity and price must be a non-negative number
                try:
                    self.qty = int(input("Quantity: "))
                    sqrt(self.qty) # To check is quantity a non-negative number
                    self.price = float(input("Price: "))
                    sqrt(self.price) # To check is price a non-negative number
                    self.dict_item[self.name] = [self.qty, self.price]
                    print(f"{self.name} added to the shopping list")
                    break
                except:
                    print("Input an actual number!")
            
    
    # Defined function to update item name on the shopping list
    def update_item_name(self):
        self.old_name = input("Previous item name: ")
        
        # Make condition when the input can't be found on the shopping list
        if self.old_name not in self.dict_item.keys():
            print(f"There's no {self.old_name} on the shopping list")
        else:
            self.new_name = input("New item name: ")
            self.dict_item[self.new_name] = self.dict_item[self.name]
            self.dict_item.pop(self.name)
            print(f"{self.old_name} changed to {self.new_name}")
    
    
    # Defined function to update item quantity on the shopping list
    def update_item_qty(self):
        self.name = input("Item name: ")
        
        # Make condition when the input can't be found on the shopping list
        if self.name not in self.dict_item.keys():
            print(f"There's no {self.name} on the shopping list")
        else:
            self.new_qty = int(input("New item quantity: "))
            self.dict_item[self.name][0] = self.new_qty
            print(f"{self.name} quantity updated")
    
    
    # Defined function to update item price on the shopping list
    def update_item_price(self):
        self.name = input("Item name: ")
        
        # Make condition when the input can't be found on the shopping list
        if self.name not in self.dict_item.keys():
            print("There's no {self.name} on the shopping list")
        else:
            self.new_price = float(input("New item price: "))
            self.dict_item[self.name][1] = self.new_price
            print(f"{self.name} price updated")
    
    
    # Defined function to delete an item on the shopping list
    def delete_item(self):
        self.name = input("Item name: ")
        
        # Make condition when the input can't be found on the shopping list
        if self.name not in self.dict_item.keys():
            print("There's no {self.name} on the shopping list")
        else:
            self.dict_item.pop(self.name)
            print(f"{self.name} deleted from the shopping list")
    
    
    # Defined function to delete all items on the shopping list
    def reset_item(self):
        self.dict_item.clear()
        print("The shopping list empty")
    
    
    # Defined function to display all items on the shopping list
    def check_order(self):
        print("\033[1m", "SHOPPING LIST", "\033[0m")
        list_item = [(key, value[0], value[1]) for key, value in self.dict_item.items()]
        print(tabulate(list_item, headers = ["Name", "Qty", "Price"], tablefmt="mixed_grid"))
        
    
    # Defined function to returns total price
    def total_price(self):
        self.total = 0
        for item in self.dict_item.keys():
            self.total += self.dict_item[item][0] * self.dict_item[item][1]
        
        # Make condition when the customers get discount
        if self.total > 500_000:
            disc = 0.1 * self.total
        elif self.total > 300_000:
            disc = 0.08 * self.total
        elif self.total > 200_000:
            disc = 0.02 * self.total
        else:
            disc = 0
        
        self.total -= disc
        
        print(f"Total price : Rp. {self.total}")
        print(f"You get discount : Rp. {disc}") if disc > 0 else None
    
    
    # Defined function to check out all items on the shopping list
    def check_out(self):
        print("Check out succeed!")

        
    # Defined function to cancel transaction
    def cancel(self):
        print("Transaction canceled!")