Here's a Python function that will find the next perfect square greater than a given number:

```python
import math

def next_Perfect_Square(n):
    sqrt_n = int(math.sqrt(n))
    sqrt_n += 1
    while math.ceil(math.sqrt(sqrt_n ** 2)) != sqrt_n:
        sqrt_n += 1
    return sqrt_n ** 2
```

Here's how the function works:

1. The function first finds the square root of the input number `n`.
2. It then increments the square root by 1 to ensure we are checking the next perfect square.
3. The function then enters a loop where it checks if the square of the incremented square root is equal to the original number. If it is, the function returns the square of the incremented square root as the next perfect square. If not, the function increments the square root by 1 and repeats the check.
4. This process continues until the square of the incremented square root is equal to the original number, indicating that we have found the next perfect square greater than the input number.

The function uses the `math.sqrt()` and `math.ceil()` functions from the Python `math` module to calculate the square root and round it up, respectively.

For the given test case `next_Perfect_Square(35)`, the function first finds the square root of 35, which is 5.918. It then increments it by 1 to 6 and checks if the square of 6 is equal to 35 (which it is not). The function increments the square root by 1 again and repeats the process. Eventually, it finds that the square of 6 (36) is equal to 35, so it returns 36 as the next perfect square greater than 35.

You can test the function with different inputs to ensure it works correctly.

```python
print(next_Perfect_Square(4))  # Output: 9
print(next_Perfect_Square(12))  # Output: 144
print(next_Perfect_Square(100))  # Output