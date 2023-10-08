"""
1. a program that prompts the user for the max number of items to be shipped 
2. allow user enter the weight of each item, one by one 
3. if over 20 kg on the current package then send and start the new package 
4. item = 0  then terminate the program 
5. display the infromation: 
    - Number of packages sent
    - Total weight of packages sent
    - Total 'unused' capacity (non-optimal packaging). This is calculated as the number of packages sent multiplied by 20 kg, minus the total weight of packages sent.
    - The package number that had the most 'unused' capacity and the amount of 'unused' capacity in that package.
"""


MAX_PACKAGE_WEIGHT = 20
MIN_PACKAGE_WEIGHT = 1
ITEM_WEIGHT_MAX = 10 

items_to_be_shipped = input ("Enter the number that need to be ship")

number_packages_sent = 0 
total_weight_package = 0 
index_most_empty_package = 0
weight_sent = 0 

correct_items = 0 

while correct_items < items_to_be_shipped: 
    print("")