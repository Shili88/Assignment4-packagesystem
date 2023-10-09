MAXIMUM_PACKAGE_WEIGHT = 20 
MINIMUM_PACKAGE_WEIGHT = 1
MAXIMUM_PACKAGE_WEIGHT = 10 

items_to_be_shipped = int(input("Please enter the number of the items: "))

package_weight = 0 
weight_sent = 0 
number_of_package_sent = 0 
index_must_empty_package = 0
lightest_package = 20 
correct_items = 0 

while correct_items < items_to_be_shipped:
    item_weight = int(input("Please enter the item weight: "))
    if item_weight == 0: 
        print("Unable to proceed")
        break
    elif item_weight < 1 or item_weight > 10:
        print("You must enetred the weights betweeen 1 to 10") 
        continue 
    else:
        correct_items += 1
        package_weight += item_weight
        if package_weight > 20:
            package_weight -= item_weight 
            number_of_package_sent +=1
            weight_sent += package_weight
            if package_weight < lightest_package:
                lightest_package = package_weight
                index_most_empty_package = number_of_package_sent
            package_weight = item_weight
else: 
    if package_weight > 0: 
        number_of_package_sent += 1
        weight_sent += package_weight
        print(package_weight)
        if package_weight < lightest_package: 
            lightest_package = package_weight
            index_most_empty_package = number_of_package_sent

unused_capacity = number_of_package_sent * 20 - weight_sent

print(f"Number of package sent: {number_of_package_sent}")
print(f"Total weight of package sent: {weight_sent}")
print(f"Total Unused capacity: {unused_capacity}")
print(f"Package number with the most unused kilograms: {index_most_empty_package}")