To solve this problem, we can check if one of the numbers is equal to the sum of the other two, and all numbers are integers.

Here's a step-by-step explanation of the solution:

1. Define the function any_int that takes three arguments: x, y, and z.
2. Check if x is equal to the sum of y and z using the equality operator (==). If it's true, return True.
3. Check if y is equal to the sum of x and z using the equality operator (==). If it's true, return True.
4. Check if z is equal to the sum of x and y using the equality operator (==). If it's true, return True.
5. If none of the previous conditions are met, return False.
6. Finally, return the result of the function.

Here's the code for the solution:

```python
def any_int(x, y, z):
    if x == y + z or y == x + z or z == x + y:
        if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
            return True
    return False
```

You can use the function like this:

```python
print(any_int(5, 2, 7))  # Output: True
print(any_int(3, 2, 2))  # Output: False
print(any_int(3, -2, 1))  # Output: True
print(any_int(3.6, -2.2, 2))  # Output: False
```

This function will return True if one of the numbers is equal to the sum of the other two, and all numbers are integers. Otherwise, it will return False.

I hope this helps! Let me know if you have any more questions.

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
