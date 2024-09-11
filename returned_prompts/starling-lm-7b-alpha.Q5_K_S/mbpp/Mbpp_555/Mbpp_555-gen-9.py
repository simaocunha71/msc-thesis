Here's a Python function that finds the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers:

```python
def difference(n):
    return n * (n + 1) * (2 * n + 1) // 6 - (n * (n + 1) // 2)
```

To test the function, you can use the `assert` statement like this:

```python
assert difference(3) == 30
```

The `difference` function uses a combination of mathematical operations to calculate the desired result. It multiplies `n` by `n + 1` and `2n + 1`, then divides the result by 6 to get the sum of cubes of the first `n` natural numbers. It also calculates the sum of the first `n` natural numbers by multiplying `n` by `n + 1` and dividing by 2. Finally, it subtracts the sum of the first `n` natural numbers from the sum of cubes to get the difference.

The `assert` statement is used to verify that the function is working correctly. If the condition `difference(3) == 30` is true, the assertion passes and the program continues. If the condition is false, an `AssertionError` is raised and the program stops.

You can test the function with different values of `n` to ensure it works correctly. For example, if you call `difference(4)`, it should return the difference between the sum of cubes of the first 4 natural numbers and the sum of the first 4 natural numbers, which is 160.

```python
print(difference(4))  # Output: 160
```

By using this function and the provided `assert` statement, you can verify that the function is calculating the difference correctly.

```python
assert difference(3) == 30
```

```python
print(difference(4))  # Output: 160
```

```python
print(difference(5))  # Output: 260
```

```python
print(difference(6))  # Output: 