def max_val(lst):
    return max(lst, key=lambda x: x if isinstance(x, int) else float('-inf'))

print(max_val(['Python', 3, 2, 4, 5, 'version'])) # Output: 5

Explanation:
The function max_val takes a list as input. The built-in Python function max is used with a key argument, which is a function that takes an element and returns a value that is used to compare the elements. The lambda function is used to define an anonymous function that returns x if x is an integer and -inf (negative infinity) otherwise, which makes max return the maximum value among all integers in the list. The isinstance function is used to check if x is an integer.
"""
