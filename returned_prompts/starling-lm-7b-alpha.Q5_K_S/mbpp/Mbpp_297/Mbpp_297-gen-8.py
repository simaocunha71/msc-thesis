"""
Here is a function that flattens a nested list:

def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if type(item) == list:
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

To use this function, you can simply call it with your desired nested list as an argument:

flattened_list = flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])
print(flattened_list)
"""

The code above defines a function called `flatten_list` that takes in a nested list as an argument. It initializes an empty list called `flattened_list` to store the flattened result.

The function then iterates over each item in the `nested_list`. If the item is of type `list`, the function recursively calls itself with the item as the argument, and extends the `flattened_list` with the result of the recursive call. This process continues until all nested lists have been flattened.

If the item is not a list, it is directly appended to the `flattened_list`. This ensures that all non-list items are included in the final flattened list.

After iterating through all items in the `nested_list`, the function returns the `flattened_list`.

To use this function, you can call it with your desired nested list as an argument. In the example provided, the function is called with the nested list `[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]`, and the result is stored in the `flattened_list` variable. Finally, the flattened list is printed to the console using `print(flattened_list)`.

The expected output