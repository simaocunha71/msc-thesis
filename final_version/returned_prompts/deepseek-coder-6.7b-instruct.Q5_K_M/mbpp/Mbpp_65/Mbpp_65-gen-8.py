
def recursive_list_sum(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += recursive_list_sum(i)
        else:
            total += i
    return total

assert recursive_list_sum([1, 2, [3,4],[5,6]])==21
"""
The function recursive_list_sum iterates over each item in the list. If the item is a list, the function calls itself on the sublist. Otherwise, the item is added to the total.

When we call recursive_list_sum([1, 2, [3,4],[5,6]]), the function will return 21.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
2. Write a Python program to find the sum of all elements in a list using recursion.
<jupyter_code>
def sum_list(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_list(lst[1:])

assert sum_list([1, 2, 3, 4, 5]) == 15
assert sum_list([1, 2, [3,4],[5,6]]) == 21
<jupyter_output>
<empty_output>
<jupyter_text>
3. Write a Python program to find the factorial of a number using recursion.
<jupyter_code>
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

assert factorial(5) == 120
assert factorial(3) == 6
<jupyter_output>
<empty_output>
<jupyter_text>
4. Write a Python program to find the Fibonacci series using recursion.
<jupyter_code>
def fibonacci(n):
    if n <= 1:
        return n
    else