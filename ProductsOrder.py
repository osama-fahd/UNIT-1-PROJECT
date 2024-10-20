from ProductsCart import ProductsCart
from Customers import Customer
import os
import json
import pickle

class ProductsOrder:
    def __init__(self, customer:Customer, cart:ProductsCart):
        self.cart = cart
        self.customer = customer
        self.__previous_products_orders = self.__load_from_json()[self.customer.username]
        
    def order_summary(self):
        print(f"Product order summary for {self.name}:")
        self.cart.display()
        print(f"\nTotal cost: SAR {self.cart.total_cost()}")
    
    def checkout_cart(self):    
        self.__previous_products_orders[len(self.__previous_products_orders) + 1] = self.cart
        self.__save_to_file(self.__previous_products_orders)
        self.__Reset_ProductsCart()
    
    def __Reset_ProductsCart(self):
        self.cart = ProductsCart()
        
    def get_previous_products_orders(self):
        return self.__previous_products_orders
           
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
    