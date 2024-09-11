def remove_elements(list_1, list_2):
    # Iterate through list_2
    for elem in list_2:
        # Remove all occurrences of elem in list_1
        while elem in list_1:
            list_1.remove(elem)
    return list_1

# Test the function
print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))
# Expected output: [1, 3, 5, 7, 9, 10]

# Test with an empty list
print(remove_elements([1, 2, 3], []))
# Expected output: [1, 2, 3]

# Test with a list with only one element
print(remove_elements([1], [1]))
# Expected output: []

# Test with a list with only one element, which is also in list_2
print(remove_elements([1], [1]))
# Expected output: []


# Test with a list with one element, which is not in list_2
print(remove_elements([1], [2]))
# Expected output: [1]

# Test with an empty list
print(remove_elements([], []))
# Expected output: []

# Test with a list with no elements in common
print(remove_elements([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 3, 4]))
# Expected output: [1, 5, 7, 9, 11, 13, 15, 17, 19]

# Test with a list with all elements in common
print(remove_elements([1, 2, 3], [1, 2, 3]))
# Expected output: []



# The above function removes all occurrences of the elements in the second list from the first list. However, it does not maintain the order of the elements in the first list. In case the order