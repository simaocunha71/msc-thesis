To solve this problem, you can use the following algorithm:

1. Initialize a variable `total` to 0. This variable will store the sum of numbers from 1 to `n`.
2. Use a loop to iterate from 1 to `n`. For each number `i` in the range, add it to the `total` variable.
3. After the loop is finished, the `total` variable will contain the sum of all numbers from 1 to `n`.
4. Return the `total` variable as the result.

Here's the code for the `sum_to_n` function using the algorithm above:

```python
def sum_to_n(n: int):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```

You can test the function with different values of `n` to verify its correctness.

For example:

```python
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

These test cases show that the `sum_to_n` function correctly calculates the sum of numbers from 1 to `n`.

Note: The algorithm uses a loop to iterate from 1 to `n`, adding each number to the `total` variable. This is an efficient approach because it only requires a single pass through the range of numbers.

I hope this helps! Let me know if you have any more questions.

```python
```

```python
```