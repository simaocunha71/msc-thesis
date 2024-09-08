def intersect_lists(list1, list2):
    return [value for value in list1 if value in list2]

print(intersect_lists([1, 2, 3, 4], [3, 4, 5, 6]))

# Output: [3, 4]

# This function uses a list comprehension to iterate over each value