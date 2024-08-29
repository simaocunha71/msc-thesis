
def common_elements(lst1, lst2):
    return [value for value in lst1 if value in lst2]

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]

"""
The function `common_elements` returns a new list that contains the common elements between two input lists.
This is done by using a list comprehension to iterate over each value in the first list `lst1`, and checking if that value is also in the second list `lst2`. If the value is in `lst2`, it is included in the new list.
