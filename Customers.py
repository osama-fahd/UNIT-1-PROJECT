from ProductsCart import ProductsCart
import os
import pickle
import json

class Customer:
    def __init__(self, name:str, username:str, password:str):
        self.name = name
        self.username = username
        self.__password = password
        self.cart = ProductsCart()
        self.previous_products_orders = self.__load_from_json()[self.username]
        
    def get_password(self):
        return self.__password
    
    def products_order_summary(self):
        print(f"Product order summary for {self.name}:")
        self.cart.display()
        print(f"\nTotal cost: ${self.cart.total_cost()}")
    
    def checkout_products_cart(self):    
        self.previous_products_orders[len(self.previous_products_orders) + 1] = self.cart
        self.__save_to_file(self.previous_products_orders)
        self.__Reset_ProductsCart()
        
    def __Reset_ProductsCart(self):
        self.cart = ProductsCart()
        
    def __save_to_file(self, previous_products_orders: dict):
        with open('previous_products_orders.json', 'w') as file:
            json.dump(previous_products_orders, file)
            
    def __load_from_json(self):
        if os.path.exists('previous_products_orders.json'):
            with open('previous_products_orders.json', 'r') as file:
                return json.load(file)
        else:
            return {{}}
        
    # def save_to_file(self, customers: dict):
    #     with open("previous_products_orders", 'wb') as file:
    #         pickle.dump(customers, file)
            
    # def load_from_file(self):
    #     if not os.path.exists("previous_products_orders"):
    #         return {}  
        
    #     with open("previous_products_orders", 'rb') as file:
    #         return pickle.load(file)
    