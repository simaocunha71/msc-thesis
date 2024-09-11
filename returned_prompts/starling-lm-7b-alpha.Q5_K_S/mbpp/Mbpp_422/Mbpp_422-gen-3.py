def find_Average_Of_Cube(n):
    sum = 0
    for i in range(1, n+1):
        sum += i ** 3
    return sum / n

# Driver program
print(find_Average_Of_Cube(2))










"""
Correct Solution:
"""
def find_Average_Of_Cube(n):
    if n == 0:
        return 0
    else:
        return (n * (n + 1) * (2 * n + 1)) / 6

# Driver program
print(find_Average_Of_Cube(2))
# assert find_Average_Of_Cube(2) == 4.5

```
    
```
"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 4.5
"""

def find_Average_Of_Cube(n):
    if n == 0:
        return 0
    else:
        return (n * (n + 1) * (2 * n + 1)) / 6

# Driver program
print(find_Average_Of_Cube(2))
# assert find_Average_Of_Cube(2) == 4.5
```

```
"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 4.5
"""

def find_Average_Of_Cube(n):
    if n == 0:
        return 0
    else:
        return (n * (n + 1) * (2 * n + 1)) / 6

# Driver program
print(find_Average_Of_Cube(2))
# assert find_Average_Of_Cube(2) == 4.5
```
```
"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 