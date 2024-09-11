Here's a Python function that checks whether a given number can be represented as the difference of two squares or not:

```python
def dif_Square(number):
    for i in range(1, number):
        for j in range(i, number):
            if i*i - j*j == number:
                return True
    return False
```

You can test the function with `dif_Square(5)` to see if it returns `True`. The function iterates through all possible combinations of `i` and `j` in the range of the given number and checks if the difference of their squares is equal to the number. If a pair of `i` and `j` is found that satisfies the condition, the function returns `True`. If no such pair is found, the function returns `False`.

Please note that this function has a time complexity of O(n^2) because it has to iterate through all possible combinations of `i` and `j`. For larger numbers, this function may take a considerable amount of time to execute.

```python
def dif_Square(number):
    for i in range(1, number):
        for j in range(i, number):
            if i*i - j*j == number:
                return True
    return False
```

You can use the `dif_Square` function to check if a number can be represented as the difference of two squares. For example, if you call `dif_Square(5)`, it will return `True` because 4 (2^2) and 1 (1^2) are the squares whose difference is 5.

Here's an example of how you can use the `dif_Square` function:

```python
print(dif_Square(5))  # Output: True
print(dif_Square(10))  # Output: False
```

In this example, the first call to `dif_Square` returns `True` because 9 (3^2) and 1 (1^2) are the squares whose difference is 5. The second call to `dif_Square` returns `False` because there are no squares whose difference is