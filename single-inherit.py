class Brands:
    brand1 = "Amazon"
    brand2 = "Flipkart"
    brand3 = "OLX"

class Products(Brands):
    produc1 = "Online Ecommerce Store"
    produc2 = "Online Store"
    produc3 = "Online Buy Sell Store"
    
store = Products()
print(store.brand1 + " is an " +     store.produc1)
print(store.brand2 + " is an " + store.produc2)
print(store.brand3 + " is an " + store.produc3)