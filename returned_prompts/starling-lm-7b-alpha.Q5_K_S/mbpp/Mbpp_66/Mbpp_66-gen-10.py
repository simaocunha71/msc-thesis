def pos_count(num_list):
    return sum(1 for num in num_list if num > 0)


# Testing the function
assert pos_count([1,-2,3,-4]) == 2


# More tests
assert pos_count([-1,2,3,-4]) == 2
assert pos_count([-1,0,3]) == 2
assert pos_count([0,3]) == 1
assert pos_count([0]) == 0
assert pos_count([]) == 0

# Still more tests
assert pos_count([1,2,3]) == 3
assert pos_count([-1,2,3]) == 2
assert pos_count([-1,0,3]) == 2
assert pos_count([-1,2,3,4,5]) == 5
assert pos_count([1,2,3,4,5]) == 5
assert pos_count([1,2,3,4,5,6]) == 6
assert pos_count([6,5,4,3,2,1]) == 6

print("All tests passed.")








"""
This function is using a generator expression to create a generator that will yield True or False for each number in the list depending on whether the number is positive or not. It then uses the built-in sum function to sum the generator, which will count the number of True values (positive numbers) in the generator.
"""


"""
In Python, a generator expression is a high-performance, memory-friendly, and syntax-sugar version of a function. It is a sort of anonymous iterator that can be used like a list comprehension but doesn't create a list. Generator expressions are more memory efficient than lists and are typically used for large data sets.

Here is an example of how to use a generator expression in Python:

def generate_numbers(n):
    return (i for i in range(n))

# Create a generator expression that generates the first n odd numbers
odd_numbers = (i for i in generate_numbers(100) if i % 2 != 0)

# Create a generator expression that generates the first n