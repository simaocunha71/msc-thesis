def remove_elements(list1, list2):
    result = []
    for i in list1:
        if i not in list2:
            result.append(i)
    return result

# Test the function
print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))
# Output: [1, 3, 5, 7, 9, 10]

# Another approach
def remove_elements_2(list1, list2):
    return [i for i in list1 if i not in list2]

# Test the function
print(remove_elements_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))
# Output: [1, 3, 5, 7, 9, 10]

# Using list comprehension in one line
def remove_elements_3(list1, list2):
    return [i for i in list1 if i not in list2]

# Test the function
print(remove_elements_3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))
# Output: [1, 3, 5, 7, 9, 10]

# Using filter function
def remove_elements_4(list1, list2):
    return list(filter(lambda x: x not in list2, list1))

# Test the function
print(remove_elements_4([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))
# Output: [1, 3, 5, 7, 9, 10]

# Using built-in function "difference"
def remove_elements_5(list1, list2):
    return list(set(