```python
def fruit_distribution(s,n):
    # Split the string into two parts: apples and oranges
    apples_oranges = s.split(' and ')
    # Convert the numbers of apples and oranges to integers
    apples, oranges = int(apples_oranges[0].split(' ')[0]), int(apples_oranges[1].split(' ')[0])
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```
