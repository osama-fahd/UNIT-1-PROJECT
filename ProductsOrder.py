from ProductsCart import ProductsCart
import os
import pickle


class ProductsOrder:
    def __init__(self, customer, cart:ProductsCart):
        self.cart = cart
        self.customer = customer
        
        self.previous_products_orders = self.__load_from_pickle()
        if not isinstance(self.previous_products_orders, dict):
            self.previous_products_orders = {}
        
    def order_summary(self):
        print(f"Product order summary for {self.customer.name}:")
        self.cart.display()
        print(f"\nTotal cost: SAR {self.cart.total_cost()}")
    
    def checkout_cart(self):  
        self.previous_products_orders[self.customer.username].append(self.cart.cart)  
        self.__save_to_file(self.previous_products_orders)
        
        print(f"Checkout successful! Your products will be arrive to you soon!.")
        self.cart.display()
        
    def get_all_products_orders(self):
        return self.__load_from_pickle()
        
    def __save_to_file(self, customers: dict):
        with open("previous_products_orders", 'wb') as file:
            pickle.dump(customers, file)
            
    def __load_from_pickle(self):
        if not os.path.exists("previous_products_orders"):
            return {}  
        
        with open("previous_products_orders", 'rb') as file:
            return pickle.load(file)
    
    