"""
def remove_elements(list1, list2):
    for i in list2:
        while i in list1:
            list1.remove(i)
    return list1

# Testing
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
print("All tests passed")
"""

def remove_elements(list1, list2):
    return [i for i in list1 if i not in list2]

# Testing
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
print("All tests passed")


# Explanation
# The problem can be solved using list comprehension. By using the expression `[i for i in list1 if i not in list2]`, we create a new list which contains all the elements of `list1` but not present in `list2`.

# Testing
# The above solution passes all the test cases.
"""
remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9, 10]) == [2, 4, 6, 8]
remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 11]) == [1, 3, 5, 7