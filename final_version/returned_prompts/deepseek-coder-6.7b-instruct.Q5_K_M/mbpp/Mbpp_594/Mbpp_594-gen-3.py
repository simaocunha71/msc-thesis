def sum_square_evens(lst):
    return sum(x**2 for x in lst if x % 2 == 0)

print(sum_square_evens([1,2,3,4,5,6,7,8,9,10])) # 220

"""
This function works by using a generator expression to generate the squares of all the even numbers in the list and then uses the built-in sum() function to add them together.
"""

# Q4:
"""
Write a function to find the sum of squares of all odd numbers in a list.
assert sum_square_odds([1