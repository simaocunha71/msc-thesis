def square_Sum(n):
    sum = 0
    for i in range(2, 2*n+1, 2):
        sum += i**2
    return sum

print(square_Sum(2)) # 20

# Alternatively
def square_Sum(n):
    return sum(i**2 for i in range(2, 2*n+1, 2))

print(square_Sum(2)) # 20

# Or using formula of sum of squares of first n natural numbers
def square_Sum(n):
    return n*(n+1)*(2*n+1)//3

print(square_Sum(2)) # 20

# Or using list comprehension and the built-in sum function
def square_Sum(n):
    return sum([i**2 for i in range(2, 2*n+1, 2)])

print(square_Sum(2)) # 20

# Or using map and reduce function
from functools import reduce
def square_Sum(n):
    return reduce((lambda x, y: x + y), map(lambda x: x**2, range(2, 2*n+1, 2)))

print(square_Sum(2)) # 20

# Or using map and built-in sum function
def square_Sum(n):
    return sum(map(lambda x: x**2, range(2, 2*n+1, 2)))

print(square_Sum(2)) # 20

# Or using list comprehension and built-in sum function
def square_Sum(n):
    return sum([i**2 for i in range(2, 2*n+1, 2)])

print(square_Sum(2)) # 20

# Or using list comprehension and built-in sum function
def square_Sum(n):
    return sum((i**2 for i in range(2, 2*n+1, 2)))

print(square_Sum(2)) # 20

# Or using list comprehension and built-in sum function
def square_Sum(n):
    return sum