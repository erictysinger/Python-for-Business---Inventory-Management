# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Eric Tysinger - etysinge@purdue.edu
# Leo Zheng - zheng702@purdue.edu

import json 
import pickle
from datetime import datetime
product_catalog = {
    '01': {'Product Name': 'T-Shirt', 'price': 10, 'Stock': 100},
    '02': {'Product Name': 'Pants', 'price': 30, 'Stock': 100},
    '03': {'Product Name': 'Hat', 'price': 15, 'Stock': 25},
    '04': {'Product Name': 'Sweater', 'price': 45, 'Stock': 75},
    '05': {'Product Name': 'Jacket', 'price': 80, 'Stock': 75},
    '06': {'Product Name': 'Shoes', 'price': 70, 'Stock': 50},
    '07': {'Product Name': 'Underwear', 'price': 5, 'Stock': 25},
    '08': {'Product Name': 'Socks', 'price': 5, 'Stock': 25},
    '09': {'Product Name': 'Tank Top', 'price': 10, 'Stock': 50},
    '10': {'Product Name': 'Pajamas', 'price': 20, 'Stock': 25}
}

# implement feature to update price and stock of products


# Initialize the lists for the menu
sales_history = []
# add placeholders for variables
sales_statistics = ['total revenue', 'best selling product', 'highest revenue product']


# Function to display the catalog
def view_catalog():
    for entry in product_catalog.items():
        print("\n", entry)
    #Your code to print the entire catalog goes here

# Function to make a sale
def make_sale():
    view_catalog()
    product_id = input("Product_Id you would like to purchase: ")
    # error handling
    while product_id not in product_catalog:
        print("Invalid Product_Id")
        product_id = input("Product_Id you would like to purchase: ")

    quantity = int(input("Quantity: "))
    while quantity > product_catalog[f"{product_id}"]["Stock"]:
        print("Quantity must be fewer than stock")
        quantity = int(input("Quantity: "))
    product_catalog[f"{product_id}"]["Stock"] -= quantity
    
    # update sales_history list
    sales = {
        'sale_id': (len(sales_history) + 1),
        'date_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'product_id': product_id,
        'product_name': product_catalog[product_id]["Product Name"],
        'quantity': quantity,
        'total_amount': product_catalog[product_id]["price"] * quantity
            }
    sales_history.append(sales)
    
    # update sales_statistics list
    total_revenue = sum(sales['total_amount'] for sales in sales_history)
    sales_statistics[0] = (f"Total Revenue: {total_revenue}")
    
    # initialize product sales dict to compute best selling product
    product_sales = {}
    for sales in sales_history:
        if sales['product_id'] in product_sales:
            product_sales[sales['product_id']] += sales['quantity']
        else:
            product_sales[sales['product_id']] = sales['quantity']
    
    best_selling_product_id = max(product_sales, key=product_sales.get)
    best_selling_product = product_catalog[best_selling_product_id]["Product Name"]
    sales_statistics[1] = (f"Best Selling Product: {best_selling_product}")
    
    # initialize another product sales dict to compute highest revenue product
    product_sales_1 = {}
    for sales in sales_history:
        if sales['product_id'] in product_sales_1:
            product_sales_1[sales['product_id']] += sales['total_amount']
        else:
            product_sales_1[sales['product_id']] = sales['total_amount']
    
    highest_revenue_product_id = max(product_sales_1, key=product_sales_1.get)
    highest_revenue_product = product_catalog[highest_revenue_product_id]["Product Name"]
    sales_statistics[2] = (f"Highest Revenue Product: {highest_revenue_product}")
    

# Function to view sales history
def view_sales_history():
    print(sales_history)

# function to view sales statistics
def view_sales_statistics():
    print(sales_statistics)

# function to save and load data
def save_and_load_data():
    global product_catalog, sales_history
    choice1 = input("Would you like to save or load a file?:")
    if choice1 == "Save":
        with open('HW2.json', 'w') as f:
            json.dump([product_catalog, sales_history], f)
        print("Data Saved")
    elif choice1 == "Load":
        with open('HW2.json', 'r') as f:
            product_catalog, sales_history = json.load(f)
    else:
        print("Invalid choice")
        

# Main program loop
while True:
    print("\nMain Menu:")
    print("1. View Catalog")
    print("2. Make a Sale and view Sales Statistics")
    print("3. View Sales History")
    print("4. Save or Load Data")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        view_catalog()
    elif choice == '2':
        make_sale()
        view_sales_statistics()
    elif choice == '3':
        view_sales_history()
    elif choice == '4':
        save_and_load_data()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
