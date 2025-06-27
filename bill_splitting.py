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
    print(get_customer_bill(name_args))
              
def get_customer_bill(name_args):
    customer_profile = get_customer_profile()

    if name_args in customer_profile.keys():
           
        customer_meal = get_customer_meal(customer_profile, name_args)
        price_list = customer_profile[name_args].get("price")

        total_bill = sum(price_list)
            
        return f"{name_args} should pay {total_bill}. They had {', '.join(customer_meal)}"
    else:
        return f"{name_args} did not have dinner"

def get_customer_meal(profile, key):
    return profile[key].get("meal")

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
    parser.add_argument("name_key", type=str, help="Gets bill for customer_profile")
    args = parser.parse_args()
    name_args = (args.name_key)
   
    main(name_args)


if __name__ == "__main__":
    run()



# TODO (extra):
# * Change the program so that it additionally reports a breakdown of what each
#   person had to eat.
# * Change the program so that if it is called without arguments, a table of
#   how much everybody should pay is displayed
