def fruit_distribution(s, n):
    apples, oranges = map(int, re.findall(r'\d+', s))
    return n - apples - oranges

print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
print(fruit_distribution("200 apples and 3 oranges", 300)) # Output: 197
print(fruit_distribution("10 apples and 10 oranges", 25)) # Output: 5
print(fruit_distribution("2 apples and 3 oranges", 20)) # Output: 15
print(fruit_distribution("4 apples and 6 oranges", 100)) # Output: 90
print(fruit_distribution("100 apples and 100 oranges", 200)) # Output: 0
print(fruit_distribution("5 apples and 10 oranges", 15)) # Output: 0
print(fruit_distribution("1 apples and 1 oranges", 2)) # Output: 0

C:
import re

def fruit_distribution(s, n):
    apples, oranges = map(int, re.findall(r'\d+', s))
    return n - apples - oranges

print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
print(fruit_distribution("200 apples and 3 oranges", 300)) # Output: 197
print(fruit_distribution("10 apples and 10 oranges", 25)) # Output: 5
print(fruit_distribution("2 apples and 3 oranges", 20)) # Output: 15
print(fruit_distribution("4 apples and 6 oranges", 100)) # Output: 90
print(fruit_distribution("100 apples and 100 oranges", 200)) # Output: 0
print(fruit_distribution("5 apples and 10 oranges", 15)) # Output: 