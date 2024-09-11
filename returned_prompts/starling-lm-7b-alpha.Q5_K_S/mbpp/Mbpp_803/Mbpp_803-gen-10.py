To check if a given number is a perfect square, we can use the following steps:

1. Take the square root of the given number using the `sqrt()` function from the `math` module.
2. If the square root is an integer, then the given number is a perfect square. Otherwise, it's not.

Here's a Python function that implements these steps:

```python
import math

def is_perfect_square(num):
    if num < 0:
        return False
    sqrt = math.sqrt(num)
    return int(sqrt) ** 2 == num
```

In this function, we first check if the number is less than 0. If it is, we return `False` because a perfect square cannot be negative. 

Next, we calculate the square root of the number using `math.sqrt()` and store it in the variable `sqrt`. 

Finally, we check if `sqrt` is an integer by converting it to an integer using `int()`. If the result of squaring `sqrt` is equal to the original number, then the number is a perfect square and we return `True`. Otherwise, it's not and we return `False`.

For example, if we call `is_perfect_square(10)`, the function will return `False` because 10 is not a perfect square.

I hope this helps! Let me know if you have any more questions.

```python
import math

def is_perfect_square(num):
    if num < 0:
        return False
    sqrt = math.sqrt(num)
    return int(sqrt) ** 2 == num
```

Here's an example usage of the function:

```python
print(is_perfect_square(16))  # True
print(is_perfect_square(25))  # True
print(is_perfect_square(10))  # False
```

As you can see, the function correctly identifies whether a number is a perfect square or not.

```python
import math

def is_perfect_square(num):
    if num < 0:
        return False
    sqrt