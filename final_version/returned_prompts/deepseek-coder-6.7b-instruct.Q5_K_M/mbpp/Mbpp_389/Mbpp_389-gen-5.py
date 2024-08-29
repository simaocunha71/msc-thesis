def find_lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1

    lucas_0 = 2
    lucas_1 = 1

    for _ in range(2, n + 1):
        lucas_0, lucas_1 = lucas_1, lucas_0 + lucas_1

    return lucas_1

assert find_lucas(9) == 76

# 1.2 Fibonacci sequence
"""
Lucas numbers are similar to Fibonacci numbers, but start with 2 and 1 instead of 0 and 1. 

Write a function to find the n'th Fibonacci number.
assert find_fibonacci(9) == 34
"""

def find_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib_0 = 0
    fib_1 = 1

    for _ in range(2, n + 1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1

    return fib_1

assert find_fibonacci(9) == 34

# 1.3 Binary Search
"""
Write a function to perform a binary search.
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == True
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11) == False
"""

def binary_search(lst, x):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == x:
            return True
        elif lst[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return False

assert binary_