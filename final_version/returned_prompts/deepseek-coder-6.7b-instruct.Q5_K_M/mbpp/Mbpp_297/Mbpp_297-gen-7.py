def flatten_list(nested_list):
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            for j in i:
                flat_list.append(j)
        else:
            flat_list.append(i)
    return flat_list

print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))

# Alternate Solution using recursion
def flatten_list_recursion(nested_list):
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(flatten_list_recursion(i))
        else:
            flat_list.append(i)
    return flat_list

print(flatten_list_recursion([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))

# Alternate Solution using List Comprehension
def flatten_list_comprehension(nested_list):
    return [i for sublist in nested_list for i in (flatten_list_comprehension(sublist) if isinstance(sublist, list) else [sublist])]

print(flatten_list_comprehension([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))
<jupyter_output>
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
[0, 10, 20