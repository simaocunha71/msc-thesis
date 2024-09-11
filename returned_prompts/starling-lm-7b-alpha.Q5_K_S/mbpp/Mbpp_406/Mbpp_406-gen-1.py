```
def find_Parity(n):
    if n % 2 == 0:
        return False
    else:
        return True
```

The above function will return True if the parity of the given number is odd, and False otherwise.

The function works by calculating the modulus of the given number with 2. If the modulus is 0, the number is even, and the function returns False. If the modulus is not 0, the number is odd, and the function returns True.

In this specific example, the function `find_Parity(12)` is called, and since 12 is an even number, the function returns False, as asserted.

In Python, the modulus operator `%` returns the remainder of the division of the first number by the second number. In this case, the modulus of 12 divided by 2 is 0, which means 12 is an even number.

The conditional expression `if n % 2 == 0:` checks if the modulus of the given number with 2 is equal to 0. If it is, the condition is true, and the function returns False. Otherwise, the condition is false, and the function returns True.

Overall, the function `find_Parity(n)` is a simple and efficient way to determine whether the parity of a given number is odd or not in Python.

Here's an example of how to use the function:

```python
print(find_Parity(12))  # Output: False
print(find_Parity(13))  # Output: True
print(find_Parity(14))  # Output: False
```

In the above code, the function `find_Parity(n)` is called with different values of `n` to demonstrate its functionality. The output shows that the function correctly determines the parity of each number, returning True for odd numbers and False for even numbers.

This function can be particularly useful in scenarios where you need to check the parity of numbers, such as in algorithms, data manipulation, or mathematical operations.

It's worth noting that the function `find_Parity(n)` is relatively straightforward and easy to understand. However, depending on the specific requirements