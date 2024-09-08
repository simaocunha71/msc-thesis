
def get_equal(lst):
    return all(len(x) == len(lst[0]) for x in lst)

print(get_equal([(11, 22, 33), (44, 55, 66)]))

"""
Explanation:

The function `get_equal` takes a list of tuples as an argument. It uses the built-in function `all` in combination with a generator expression to determine whether all tuples in the list have the same length as the first tuple in the list.

If all tuples have the same length, the `all` function will return `True`, otherwise it will return `False`.
"""
<jupyter_output>
True
<jupyter_text>
Q3:Write a Python program to calculate the sum of the numbers in the list using a recursive function.
<jupyter_code>
def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

numbers = [1, 2, 3, 4, 5]
print(recursive_sum(numbers))
<jupyter_output>
15
<jupyter_text>
Q4:Write a Python program to find the factorial of a number using recursion.
<jupyter_code>
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 5
print(f"The factorial of {num} is {factorial(num)}")
<jupyter_output>
The factorial of 5 is 120
<jupyter_text>
Q5:Write a Python program to find the sum of squares of first n natural numbers using recursion.
<jupyter_code>
def sum_of_squares(n):
    if n == 1:
        return 1
    else:
        return n*n + sum_of_squares(