
To find the greatest common divisor of two numbers a and b, you can use the Euclidean algorithm. Here's a step-by-step explanation of how the algorithm works:

1. If one of the numbers is zero, then the other number is the greatest common divisor.
2. If both numbers are non-zero, find the remainder of the division of the larger number by the smaller number.
3. Replace the larger number with the smaller number and the smaller number with the remainder obtained in step 2.
4. Repeat steps 2 and 3 until the remainder becomes zero, then the other number is the greatest common divisor.

In Python, you can implement the Euclidean algorithm as follows:

```python
def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
```

This function takes two integers `a` and `b` as input and returns their greatest common divisor. The algorithm uses a `while` loop to repeatedly update the values of `a` and `b` until the remainder becomes zero. Finally, it returns the value of `a`, which is the greatest common divisor.

You can test the function with the provided examples:

```python
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

These tests verify that the `greatest_common_divisor` function correctly computes the greatest common divisor of the given input numbers.

By using the Euclidean algorithm, you can efficiently find the greatest common divisor of two integers, even for large values of `a` and `b`.

Here are some additional examples of using the `greatest_common_divisor` function:

```python
print(greatest_common_divisor(48, 18))  # Output: 6
print(greatest_common_divisor(99, 73))  # Output: 1
```

In these examples, the