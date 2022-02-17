class Brands:
    brand1 = "Amazon"
    brand2 = "Flipkart"
    brand3 = "OLX"

class Products(Brands):
    produc1 = "Online Ecommerce Store"
    produc2 = "Online Store"
    produc3 = "Online Buy Sell Store"
    
class Popularity(Products):
    produc1_pop = 100
    produc2_pop = 80
    produc3_pop = 60

store = Popularity()

print(store.brand1 + " is an " + store.produc1 + " popularity is ", store.produc1_pop)
print(store.brand2 + " is an " + store.produc2 + " popularity is ", store.produc2_pop)
print(store.brand3 + " is an " + store.produc3 + " popularity is ", store.produc3_pop)