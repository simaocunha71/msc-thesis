def find_lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return find_lucas(n-1) + find_lucas(n-2)

def find_lucas_recursive(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return find_lucas_recursive(n-1) + find_lucas_recursive(n-2)

def find_lucas_iterative(n):
    a, b = 2, 1
    for _ in range(n-1):
        a, b = b, a+b
    return a

print(find_lucas(9))
print(find_lucas_recursive(9))
print(find_lucas_iterative(9))
# Output: 76, 76, 76

"""
The lucas numbers are a sequence of integers, defined by:
l(0) = 2
l(1) = 1
l(n) = l(n-1) + l(n-2)

The problem asks you to write a function to find the nth lucas number, which you can do with a simple recursive function:

def find_lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return find_lucas(n-1) + find_lucas(n-2)

This function will return the nth lucas number, but it's not very efficient: the same subproblems are solved over and over again. To speed it up, you can use memoization, a technique that involves storing the results of expensive function calls and returning the cached result when the same inputs occur again:

def find_lucas(n, memo={}):
    if n == 0:
        return 2
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = find_luc