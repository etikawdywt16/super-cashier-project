# Super Cashier Project #
### Background ###
---------------
Super Cashier is a program using Python language program to create a self-service cashier system at a supermarket, so customers can make their own transactions.


### Objectives ###
---------------
1. Create a simple program using Python that has some features:
   * Add item (name, quantity, and price) to the shopping list
   * Update items (name, quantity, and price) in the shopping list
   * Delete items in the shopping list
   * Show all items in the shopping list
   * Reset items in the shopping list
   * Show total price and discount
   * Check out all items in the shopping list
   * Show history of transactions
   * Exit transaction
2. Apply modular code programming technique
3. Apply functional programming and Object Oriented Programming (OOP) concept
4. Apply PEP8 and docstring to write clean code


### Program Flowchart ##
---------------
#### Menu Flowchart ####
![Super Cashier Project Flowchart](https://user-images.githubusercontent.com/91242818/218290221-a9dbb7d4-9fa5-42cf-adfd-cba9d0c3bd63.jpg)

#### Method Flowchart ####
##### Add Item #####
![Flowchart-1](https://user-images.githubusercontent.com/91242818/215308279-4231dfe5-a1a3-40be-bd7a-30b17a7f078c.jpg)

#### Update Item Name ####
![Flowchart-2](https://user-images.githubusercontent.com/91242818/218292473-3a8611d4-b88c-46fa-8135-2d40d3656145.jpg)

#### Update Item Quantity ####
![Flowchart-3](https://user-images.githubusercontent.com/91242818/218292477-6ff4fac3-decd-4b5c-8a2d-2be01a27c075.jpg)

#### Update Item Price ####
![Flowchart-4](https://user-images.githubusercontent.com/91242818/218292478-1d29bde7-1f69-42d2-ac16-740ec5262f16.jpg)

#### Delete Item ####
![Flowchart-5](https://user-images.githubusercontent.com/91242818/218292479-6963aa1b-fd75-44cb-877d-7f20ee3cd7d0.jpg)

#### Check Order ####
![Flowchart-6](https://user-images.githubusercontent.com/91242818/215309076-88b40abc-1f22-494f-aab5-5bac39c0de1c.jpg)

#### Reset Items ####
![Flowchart-7](https://user-images.githubusercontent.com/91242818/215308710-9e227b58-8d0b-4b69-b70a-aa32ea6e72e9.jpg)

#### Total Price ####
![Flowchart-8](https://user-images.githubusercontent.com/91242818/218290288-a2fcdf06-6978-4b5b-9636-e722a6c6f874.jpg)

#### Check Out ####
![Flowchart-9](https://user-images.githubusercontent.com/91242818/218292516-87787f4b-3bf6-4b9d-aa98-509747dc422c.jpg)

#### History of Transaction ####
![Flowchart-10](https://user-images.githubusercontent.com/91242818/218292520-4998c295-cdc0-45cf-bea8-02043523c48f.jpg)


### Program Description ###
---------------
Function for each features in Super Cashier system:
![Program Description](https://user-images.githubusercontent.com/91242818/218290367-da0bfa7a-8f9a-4f9a-a7af-e0baa1f0220e.png)


### Test Case and How to Run Program ###
---------------
**1. Install library written in requirement.txt file**

**2. Run main.py**

#### Main Menu ####
![1-Menu](https://user-images.githubusercontent.com/91242818/215303213-dd4e5192-ed3b-4c0b-818b-3fdb4cadbb68.png)

#### Case 1: Add Item ####
![2-Test Case 1](https://user-images.githubusercontent.com/91242818/215303314-3a6787c7-cc76-4082-b532-95c8d3cda793.png)

In case input invalid, ex: empty name input or string type quantity and price input, then a warning is appeared to require valid input:

![3-Test Case 1](https://user-images.githubusercontent.com/91242818/215303363-4a5243f0-bfab-460f-a772-a5d9a1737421.png)

![4-Test Case 1](https://user-images.githubusercontent.com/91242818/215303365-29a90207-13df-4a65-8dd4-634447781924.png)

![5-Test Case 1](https://user-images.githubusercontent.com/91242818/215303366-c0eb69e0-c90a-4bcf-8014-01e25ed869f5.png)

#### Update Menu ####
![6-Test Case 2](https://user-images.githubusercontent.com/91242818/215303433-159bedcf-7bfc-482a-8487-5166ffea6ec0.png)

#### Case 2: Update Item Name ####
![7-Test Case 2](https://user-images.githubusercontent.com/91242818/215303454-397752d9-c0ed-4085-83f4-ba6f806a49d2.png)

#### Case 3: Update Item Quantity ####
![8-Test Case 3](https://user-images.githubusercontent.com/91242818/215303463-ee7fd680-170c-43a7-b9e6-a1ef6cfeaaef.png)

#### Case 4: Update Item Price ####
![9-Test Case 4](https://user-images.githubusercontent.com/91242818/215303467-2b411889-cef3-46ca-82ea-bb4f997c104b.png)

In case name input can't be found in the shopping list, then a warning is appeared to require available name:

![10-Test Case](https://user-images.githubusercontent.com/91242818/215303501-892cfcd9-e440-400f-b370-659f8d5908e8.png)

#### Case 5: Delete Item ####
![11-Test Case 5](https://user-images.githubusercontent.com/91242818/215303507-64d48f2b-a9f1-4892-9529-4a1107a2dee7.png)

#### Case 6: Show All Items ####
![12-Test Case 6](https://user-images.githubusercontent.com/91242818/218241069-d646741b-772a-4136-8052-eeba0aa939fe.png)

#### Case 7: Reset Item ####
![13-Test Case 7](https://user-images.githubusercontent.com/91242818/215303517-701fb5c7-101b-407c-a9e3-96c67b6c5081.png)

Shopping list after reset:

![14-Test Case 7](https://user-images.githubusercontent.com/91242818/215303523-63eac1bf-ac9f-49f3-a907-eddb5e9f2678.png)

#### Case 8: Show Total Price and Discount ####
After add some items to the shopping list:

![15-Test Case 8](https://user-images.githubusercontent.com/91242818/218241078-a9a498d8-c9a1-414c-9294-9ee7e3399a62.png)

Total price and discount:

![16-Test Case 8](https://user-images.githubusercontent.com/91242818/218290146-a6fc3f6d-ffc4-4d94-91db-88ea4799af90.png)

#### Case 9: Check Out Items ####
![17-Test Case 9](https://user-images.githubusercontent.com/91242818/215303817-c20b497d-924a-4596-ace9-445f7e5a64e0.png)

#### Case 10: Show History of Transactions ####
![18-Test Case 10](https://user-images.githubusercontent.com/91242818/218290180-58cc73c0-4092-4342-ac86-6a44a8c2f10b.png)

#### Case 11: Exit Transaction ####
![19-Test Case 11](https://user-images.githubusercontent.com/91242818/215309488-65bce7d6-dab1-41e0-affe-32845e617f49.png)


### Conclusion and Future Work ###
---------------
#### Conclusion ####
After all these processes, we have:
1. Developed class Transaction and create methods of transaction
2. Developed menu to simplify transaction

#### Future Work ####
Hope the next work we will:
1. Develop class User and create method to track transaction for each user
2. Connect program to database so user can only input available items in the database
