def flatten_list(nested_list):
    # initialize an empty list
    flattened_list = []
    # iterate through each element in the nested list
    for item in nested_list:
        # if the item is a list, recursively call the function
        if type(item) == list:
            flattened_list.extend(flatten_list(item))
        else:
            # otherwise, append the item to the flattened list
            flattened_list.append(item)
    return flattened_list

# Testing the function
print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))
# Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]




"""
Explanation:
To flatten a nested list, we need to recursively iterate through each element in the list.
If an element is a list, we recursively call the function on that element.
If an element is not a list, we append it to the flattened list.
"""

"""
Here's a step-by-step explanation of how the function works:

1. We initialize an empty list called flattened_list to store the flattened result.
2. We iterate through each item in the nested list.
3. If the item is a list, we recursively call the function on that item by using flatten_list(item).
4. If the item is not a list, we append it to the flattened_list using flattened_list.append(item).
5. After iterating through all the elements in the nested list, we return the flattened_list.
6. We test the function by passing the given nested list [0, 10, [20, 30], 40, 50, [60, 70, 