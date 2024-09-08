def flatten_list(nested_list):
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(i)
        else:
            flat_list.append(i)
    return flat_list

print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))

"""
Output:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""

# Alternative Solution using List Comprehension
def flatten_list(nested_list):
    return [i for sublist in nested_list for i in (flatten_list(sublist) if isinstance(sublist, list) else [sublist])]

print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))

"""
Output:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""

# Alternative Solution using recursion and ternary operator
def flatten_list(nested_list):
    return [flatten_list(i) if isinstance(i, list) else i for i in nested_list]

print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))

"""
Output:
[0, 