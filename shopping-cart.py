# shopping-cart.py

#from pprint import pprint

import datetime

def to_usd(my_price): #price formatting from groceeries exercise
    return "${0:,.2f}".format(my_price)


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output
#product_list = [] I tried the below code first and it worked to some extent then i ran into trouble with the formatting
#id = "x"
#while id != "DONE":
    #id = input('Please input a product id or enter DONE:') #http://introtopython.org/while_input.html
    #product_list.append(id)
#print(product_list)
subtotal = 0
tax_rate = 0.08875

valid_ids = [str(p["id"]) for p in products]
#print(valid_ids)
selected_ids = []
while True:
    selected_id = input("Please input a product id or enter 'DONE' if complete:")
    if selected_id == "DONE":
        break
    elif str(selected_id) in valid_ids:
        selected_ids.append(selected_id)
    else:
        print("INVALID INPUT, PLEASE TRY AGAIN")
        next
now = datetime.datetime.now() # current date and time. code from https://www.w3resource.com/python-exercises/python-basic-exercise-3.php

print ('-------------------------------')
print ("TRADER JOES'S") #handling apostrophe's in stringshttps://stackoverflow.com/questions/14104728/not-able-to-print-statements-with-apostrophe-in-it-in-python-invalid-syntax-e
print ('555 9th Street') #sample receipt https://www.google.com/imgres?imgurl=https://c1.staticflickr.com/1/32/64253187_429175fba8_b.jpg&imgrefurl=https://www.flickr.com/photos/evang/64253187&h=1024&w=768&tbnid=rgRZZTB5iixMNM&q=trader+joe%27s+receipt&tbnh=150&tbnw=113&usg=AI4_-kSDL59GpSZXawvPomxmAKFxum2sUg&vet=1&docid=jzZEjP2nNwMAHM&itg=1&sa=X&ved=2ahUKEwiM_8rk8OTiAhUMTN8KHabQB6IQ_h0wE3oECA0QBA#h=1024&imgdii=l4siABnz7GxBFM:&tbnh=150&tbnw=113&vet=1&w=768
print ('SAN FRANCISCO, CA 94103')
print ('STORE #078 - (415) 863-1292')
print ('-------------------------------')
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print ('-------------------------------')
print ('SELECTED PRODUCTS:')

# tried this first p for p in products: #help from https://goodcode.io/articles/python-dict-object/
    #if p['id'] in product_list:
        #print("product_list['name'] + " " + str(product_list['price_usd'])")
for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
#print(selected_ids)
#print(matching_products)
    matching_product = matching_products[0]
    subtotal = subtotal + matching_product["price"]
    price_usd = to_usd(matching_product["price"]) 
    print(matching_product["name"] + "...." + str(price_usd))
print ('-------------------------------')
subtotal_usd = to_usd(subtotal) 
print('SUBTOTAL: ' + str(subtotal_usd))

tax = subtotal * tax_rate
tax_usd = to_usd(tax)
print("TAX: " + str(tax_usd))

total = subtotal + tax 
total_usd = to_usd(total)
print("TOTAL: " + str(total_usd))
print ('-------------------------------')
print('THANK YOU FOR SHOPPING WITH US. WE HOPE TO SEE YOU SOON!')
print ('-------------------------------')





