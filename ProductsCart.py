from Products import Products

class ProductsCart:
    def __init__(self):
        self.cart = {}
        
    def add_to_cart(self, product:Products, quantity:int):
        if quantity <= product.quantity:
            if product.product_id not in self.cart[product.product_id]:
                self.cart[product.product_id] = {'product': product, 'quantity': quantity}
                product.quantity -= quantity
                return True
            else:
                newQuantity = self.cart[product.product_id]['quantity'] + quantity
                if newQuantity <= product.quantity:
                    self.cart[product.product_id]['quantity'] += quantity
                    product.quantity -= quantity
                    return True
                
        return False
        
    def display(self):
        if self.is_empty():
            return False
        else:
            for i, value in enumerate(self.cart, start=1):
                print(f'{i}. Name: {value['product'].name}, Price: {value['product'].price}, Quantity: {value['quantity']}')
                
            return True
    
    def delete_from_cart(self, product:Products, unWantedQuantity:int, all=False):
        if product.product_id in self.cart[product.product_id]:
            if unWantedQuantity <= self.cart[product.product_id]['quantity']:
                newQuantity = self.cart[product.product_id]['quantity'] - unWantedQuantity
                if all or newQuantity <= 0:
                    del self.cart[product.product_id]
                else:
                    self.cart[product.product_id]['quantity'] -= unWantedQuantity
                return True
            print('The quantity you want to delete is bigger than the actual quantity you added')
        
        return False
    
    def total_cost(self):
        totalCost = 0
        for value in self.cart.values():
            totalCost += value['product'].price * value['quantity']
            
        return totalCost