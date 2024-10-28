
Here's a simple implementation of modp function using the built-in `pow` function:

```python
def modp(n: int, p: int):
    return pow(2, n, p)
```

This function takes in two arguments, `n` and `p`, and returns the result of `2^n` modulo `p`.

For example, if you call `modp(3, 5)`, it will return `3` because `2^3` modulo `5` is equal to `3`. Similarly, `modp(1101, 101)` will return `2` and `modp(0, 101)` will return `1`.

Here's a step-by-step breakdown of how the function works:

1. The function takes in two arguments, `n` and `p`, which represent the exponent and the modulus, respectively.
2. It uses the built-in `pow` function to calculate `2^n`. The `pow` function takes three arguments: the base (`2`), the exponent (`n`), and the modulus (`p`).
3. The result of `2^n` modulo `p` is returned by the function.

You can use this function to calculate the modulo of powers of 2 efficiently.

Here are some test cases to verify the correctness of the function:

```python
print(modp(3, 5) == 3)  # True
print(modp(1101, 101) == 2)  # True
print(modp(0, 101) == 1)  # True
print(modp(3, 11) == 8)  # True
print(modp(100, 101) == 1)  # True
```

These test cases cover different scenarios and confirm that the `modp` function is working correctly.

In terms of time complexity, the `pow` function used in the `modp` function has a time complexity of O(log n), where n is the exponent. Therefore, the overall time complexity of the `modp` function is also O(log n).

Add