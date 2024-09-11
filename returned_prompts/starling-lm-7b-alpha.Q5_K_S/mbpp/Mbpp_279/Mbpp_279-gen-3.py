```
def is_num_decagonal(n):
    if n < 1:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return False
    if n % 9 == 0:
        return False
    if n % 11 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 13 == 0:
        return False
    if n % 17 == 0:
        return False
    return True
```

This function `is_num_decagonal(n)` takes in a number `n` and checks if it is a decagonal number. It returns True if `n` is a decagonal number, and False otherwise.

A decagonal number is a polygonal number that represents the sum of the first `n` decagons. The formula to calculate the `n`th decagonal number is `n * (n + 1) / 2 + n`. 

To check if a number is a decagonal number, we can use a series of modulo checks. If `n` is divisible by 2, 9, 11, 5, 13, or 17, it is not a decagonal number. If `n` is equal to 1, it is a decagonal number. 

The function `is_num_decagonal(n)` returns True if `n` is a decagonal number, and False otherwise. 

To test the function, you can use the `assert` statement. For example, `assert is_num_decagonal(3) == 27` checks if the function correctly identifies the 3rd decagonal number as 27. 

Here's an example usage of the function:
```python
print(is_num_decagonal(3))  # Output: True
```

The function `is_num_decagonal(n)` can be used to determine if a given number is a decagonal number or not.

```python
def find_nth_decagonal(n):
    for i in range(1, n + 1):
        if is_num