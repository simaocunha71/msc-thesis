def division_elements(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        result.append(tup1[i]/tup2[i])
    return result


# Test
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)


"""
Write a function that takes in two tuples and performs mathematical addition operation element-wise across the given tuples.
assert addition_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (15, 6, 9, 12)
"""

def addition_elements(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        result.append(tup1[i]+tup2[i])
    return result


# Test
assert addition_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (15, 6, 9, 12)


"""
Write a function that takes in a tuple of numbers and returns the sum of all the numbers in the tuple.
assert sum_of_numbers((1, 2, 3)) == 6
"""

def sum_of_numbers(tup1):
    result = 0
    for i in tup1:
        result += i
    return result


# Test
assert sum_of_numbers((1, 2, 3)) == 6


"""
Write a function that takes in a tuple of strings and returns a single string that is the concatenation of all the strings in the tuple, separated by a comma and space.
assert join_strings(("Hello", "World")) == "Hello, World"
"""

def join_strings(tup1):
    result = ""
    for i in range(len(tup1)):
        result += tup1[i] + ", "
    result = result.rstrip(", ")
    return result
