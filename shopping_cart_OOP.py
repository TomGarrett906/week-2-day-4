class Cart:  
    def __init__(self):
        self.cart = {}
           
    def check_shopping(self):
        user_shopping = input("\nWould you like to shop? [Y]es or [N]o: ").lower()
        return True if user_shopping in ('y','yes') else False
#input
    def check_input(self):
        if self.check_shopping():
            print("\nWelcome to the shop!\n")
            return input('Would you like to: [a]dd , [d]elete , [s]how? ').lower()       
        else:
            print("\nLeaving shop.\n")
#add
    def add_to_cart(self, item, price, quantity):
        if item not in self.cart:
            self.cart[item] = {'price': price, 'quantity': quantity}
        else:
            self.cart[item]['quantity'] += quantity
#delete
    def del_from_cart(self, item):
        if item in self.cart:
            del self.cart[item]
            print(f"Deleted {item} from the cart.")
        else:
            print(f"{item} not in cart.")        
#show
    def show_cart(self):
        total = 0
        for item, dict in self.cart.items():
            print(f"\n*Cart Item*\n\n{item}\nQuantity: {dict['quantity']}\nPrice: {dict['price']}")
            total += dict['quantity'] * dict['price']
        print(f'Your Total is: ${total:.2f}')
#driver
    def driver(self):
        while self.check_shopping():
            user_input = self.check_input()
            if user_input in ('a','add'):
                item = input("\nWhat would you like add? ")
                while True:
                    try:
                        price = float(input(f"\nHow much does the {item} cost? "))
                        break
                    except:
                        print("Please enter price in digits. EX: 5.99: ")
                while True:
                    quantity = input(f"How many {item}'s would you like to add? ")
                    if quantity.isdigit():
                        quantity = int(quantity)
                        break
                    else:
                        print("Please enter price in digits. EX: 5: ")
                self.add_to_cart(item, price, quantity)
                print(f"You added {quantity} {item}'s to the cart.")
            elif user_input in ('d','del','delete'):
                delete_item = input("\nWhich item would you like to delete? ")
                self.del_from_cart(self.cart, delete_item)
            elif user_input in ('s','show'):
                self.show_cart()
            else:             
                print("Invalid responsae, Try again!")

my_cart = Cart() 
my_cart.driver() 