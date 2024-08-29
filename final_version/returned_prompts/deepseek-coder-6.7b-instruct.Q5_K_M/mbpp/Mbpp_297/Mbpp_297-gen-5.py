def flatten_list(nested_list):
    flat_list=[]
    for i in nested_list:
        if isinstance(i, list):
            for j in i:
                flat_list.append(j)
        else:
            flat_list.append(i)
    return flat_list

print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))

"""
Output:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""

Explanation:
This function checks if each item in the given list is a list or not. If it is a list, it goes through that list and appends all its elements to the flat_list, otherwise, it just appends the item to the flat_list. This is how we flatten the nested list.
"""

# Alternative Solution:

def flatten_list(nested_list):
    flat_list = []
    for i in nested_list:
        if type(i) == list:
            flat_list.extend(i)
        else:
            flat_list.append(i)
    return flat_list

print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))

"""
Output:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""
"""
Alternative Solution Explanation:
This alternative solution uses the extend() method of the list data type which adds the elements of the list (or any iterable