
To solve this problem, you can use the Euclidean algorithm, which is an efficient method to find the greatest common divisor (GCD) of two numbers. Here's the step-by-step solution:

1. Initialize `a` and `b` as the input integers.
2. Enter a while loop that continues until `b` is equal to 0.
3. Inside the loop, calculate the remainder of `a` divided by `b` using the modulo operator `%` and assign it to a variable called `r`.
4. Update `a` by assigning `b` to it, and `b` by assigning `r` to it. This step is equivalent to swapping the values of `a` and `b`.
5. Repeat steps 3 and 4 until `b` becomes 0.
6. Once the loop is finished, the value of `a` will be the GCD of the original `a` and `b`. Return `a` as the result.

Here's the Python implementation of the solution:

```python
def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
```

You can test the function with the provided examples:

```python
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This implementation follows the Euclidean algorithm and efficiently calculates the GCD of two integers.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
```

You can test the function with the provided examples:

```python
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5