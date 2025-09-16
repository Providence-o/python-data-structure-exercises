# This program reports how much individuals should pay for their order at
# dinner.
#
# Usage:
#
# $ python bill_splitting.py [name]
#
# For instance:
#
# $ python bill_splitting.py Tom
# Tom should pay 38.55
#
# or:
#
# $ python bill_splitting.py Tim
# Tim did not have dinner

import argparse
from itertools import groupby

bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramasu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramasu', 4.90],
]

print('There are {} items on the bill'.format(len(bill_items)))


# TODO:
# * Implement the program as described in the comments at the top of the file.

description = "This program reports how much individuals should pay for their bill at dinner"

def main(name_args):
    if not name_args:
        print(get_table_bill())
    else:
        print(get_customer_bill(name_args))

def get_customer_bill(name_args):
    order_profile = get_table_profile()

    matched_name = None
    for customer_name in order_profile.keys():
        if name_args.lower() == customer_name.lower():
            matched_name = customer_name
           
    if not matched_name:
        return f"{name_args} did not have dinner"
    
    for _, order_items in order_profile.items():
        customer_meal = order_items.get("meal")

        order_total = order_items.get("amount_due")
        
    return f"{matched_name} should pay {order_total}. They had {customer_meal}"
       

def get_table_bill():
    table_bill = get_table_profile()

    table = ["\nCustomer\tMeal\t\t\t\t\t\t\tTotal"]
    
    for customer, order in table_bill.items():
        meal = order.get("meal")
        order_total = order.get("amount_due")
        items = f"{customer:<13}{meal:<60}{order_total}"
        table.append(items)
    return "\n".join(table)


def get_table_profile():
    table_profile = get_customer_profile()

    for _, order in table_profile.items():
        price_list = order.get("price")
        total_bill = sum(price_list)

        order["amount_due"] = total_bill

        customer_meal = order.get("meal")
        customer_meal_str = ', '.join(customer_meal)
        order["meal"] = customer_meal_str
     
    return table_profile

def get_customer_profile():
    customer_profile = {}
    
    name_key = lambda x: x[0]
   
    sorted_bill_items = sorted(bill_items, key=name_key)
    
    for name, bill in groupby(sorted_bill_items, name_key):
        meal_item = []
        item_price = []
        for _, meal, price in bill:
            meal_item.append(meal)     
            item_price.append(price)

        customer_profile[name] = {"meal": meal_item, "price": item_price}

    return customer_profile

def run():
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("customer_name", type=str, nargs="?", help="Calculates bill for a given customer")
    args = parser.parse_args()
    name_args = (args.customer_name)
   
    main(name_args)


if __name__ == "__main__":
    run()



# TODO (extra):
# * Change the program so that it additionally reports a breakdown of what each
#   person had to eat.
# * Change the program so that if it is called without arguments, a table of
#   how much everybody should pay is displayed
