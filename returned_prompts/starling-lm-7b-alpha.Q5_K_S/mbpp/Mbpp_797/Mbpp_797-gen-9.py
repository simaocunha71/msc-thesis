Here's a Python function that should solve your problem:

```python
def sum_in_range(l,r):
    total = 0
    for i in range(l,r+1):
        if i % 2 != 0:
            total += i
    return total
```

This function first initializes a variable `total` to 0. Then it loops over all numbers in the range `[l,r+1]`. For each number, it checks if it's odd by taking its modulus with 2 and checking if the result is not equal to 0. If the number is odd, it adds it to the `total`. Finally, it returns the `total` after the loop is finished.

To test the function, you can use an assert statement as follows:

```python
assert sum_in_range(2,5) == 8
```

This will raise an error if the function doesn't return the expected result for the given input.

To use the function, you can simply call it with the desired range `[l,r]`:

```python
result = sum_in_range(2,5)
print(result)  # Prints: 8
```

This will print the sum of all odd natural numbers in the range `[2,5]`, which is 8.

```python
```

Here's a step-by-step breakdown of how the function works:

1. Initialize `total` to 0. This variable will store the sum of all odd numbers in the range.
2. Loop over all numbers in the range `[l,r+1]`. For each number, check if it's odd by taking its modulus with 2 and checking if the result is not equal to 0. If the number is odd, add it to the `total`.
3. After the loop is finished, return the `total`. This will be the sum of all odd natural numbers in the range.
4. Use an assert statement to check if the function returns the expected result for the given input. If it doesn't, an error will be raised.
5. Call the function with the desired range `[l,r]` to get the sum of all odd natural numbers in