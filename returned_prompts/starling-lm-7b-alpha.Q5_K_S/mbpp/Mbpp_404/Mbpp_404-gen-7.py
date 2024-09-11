minimum = lambda x, y: x if x < y else y

assert minimum(1,2) == 1

"""
Write a python function to find the maximum of two numbers.
assert maximum(1,2) == 2
"""

maximum = lambda x, y: x if x > y else y

assert maximum(1,2) == 2

"""
Write a python function to find the minimum of three numbers.
assert minimum(1,2,3) == 1
"""

minimum = lambda *args: min(args)

assert minimum(1,2,3) == 1

"""
Write a python function to find the maximum of three numbers.
assert maximum(1,2,3) == 3
"""

maximum = lambda *args: max(args)

assert maximum(1,2,3) == 3

"""
Write a python function to find the factorial of a number.
assert factorial(1) == 1
assert factorial(3) == 6
"""

factorial = lambda x: 1 if x == 1 else x * factorial(x-1)

assert factorial(1) == 1
assert factorial(3) == 6

"""
Write a python function to find the factorial of a number using recursion.
assert factorial_recursion(1) == 1
assert factorial_recursion(3) == 6
"""

factorial_recursion = lambda x: 1 if x == 1 else x * factorial_recursion(x-1)

assert factorial_recursion(1) == 1
assert factorial_recursion(3) == 6

"""
Write a python function to find the sum of all the numbers from 1 to n.
assert sum_of_numbers(1) == 1
assert sum_of_numbers(3) == 6
"""

sum_of_numbers = lambda n: n * (n + 1) // 2

assert sum_of_numbers(1) == 1
assert sum_of_numbers(3) == 6

"""
Write a python function to find