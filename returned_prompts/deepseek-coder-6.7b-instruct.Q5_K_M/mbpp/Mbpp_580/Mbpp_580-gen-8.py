
def extract_even(tup):
    result = []
    for item in tup:
        if type(item) == tuple:
            new_item = extract_even(item)
            if new_item:
                result.append(new_item)
        elif item % 2 == 0:
            result.append(item)
    return tuple(result)

print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)))  # Output: (4, (6, (2, 4)), 6, 8)

This solution works by recursively traversing the input tuple and if the current item is an even number, it adds it to the result list. If the current item is a sub-tuple, it recursively calls the `extract_even` function on the sub-tuple and if the result is not empty, it adds the result to the result list. The function finally returns a tuple of all even numbers found in the input tuple.
"""

# Q2:
"""
Write a function that takes a list of numbers and returns the sum of the squares of all the numbers in the list.
assert sum_of_squares([1, 2, 3, 4, 5]) == 55
"""

A2:

def sum_of_squares(lst):
    return sum(i**2 for i in lst)

print(sum_of_squares([1, 2, 3, 4, 5]))  # Output: 55

This solution works by using a generator expression inside the `sum` function. The generator expression generates the square of each number in the list and the `sum` function adds up all these squares.
"""

# Q3:
"""
Given a list of numbers, write a function to return a dictionary where the keys are the numbers in the list and the values are the squares of the numbers.
assert squares_dict([1, 2, 3, 4, 5]) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

A3:

def squares_dict(