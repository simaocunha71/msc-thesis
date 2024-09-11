def is_perfect_square(n):
    x = int(n**.5)
    return x*x == n

# Test Cases
print(is_perfect_square(25))  # True
print(is_perfect_square(10))  # False

"""
A perfect square is a number that can be expressed as the product of an integer with itself.
For example, 9 is a perfect square because 3*3 = 9.
"""

"""
To check whether a number is a perfect square or not, we can follow these steps:

Find the square root of the given number using the exponentiation operator (**). Since the result is an integer, we can use the int() function to convert the result to an integer.
Check if the square of the integer obtained in the previous step is equal to the original number.
If it is equal, then the number is a perfect square. Otherwise, it is not a perfect square.
In the given solution, the is_perfect_square() function follows these steps to check if a number is a perfect square or not.
"""

```python
def is_perfect_square(n):
    x = int(n**.5)
    return x*x == n
```

The is_perfect_square() function takes a number as input and returns True if the number is a perfect square, and False otherwise. It works by finding the square root of the given number using the exponentiation operator (**), converting the result to an integer using the int() function, and then checking if the square of the integer is equal to the original number. If it is equal, the function returns True; otherwise, it returns False.
```python
# Test Cases
print(is_perfect_square(25))  # True
print(is_perfect_square(10))  # False
```

In the test cases, we can see that the function correctly identifies whether the given numbers are perfect squares or not. The first test case, 25, is a perfect square (5*5 = 25), so the function returns True. The second test case, 10, is not a perfect square, so the function returns False.
```python
"""
To check whether a number is a perfect