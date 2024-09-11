```
def decimal_to_binary(n):
    s = ''
    while n:
        s += str(n % 2)
        n //= 2
    return s[::-1]
```

This function works by repeatedly dividing the number by 2 and appending the remainder to the left of the result string. The result is then reversed to get the correct binary representation, as in the example 8/2=4, 4/2=2, 2/2=1, 1/2=0, and thus 8 in binary is 1000.

Alternatively, you can use Python's built-in bin() function to convert a decimal number to binary. However, it will include a '0b' prefix which indicates that the number is in binary, so you will need to remove this prefix if you don't want it. Here's an example function that uses bin() and removes the '0b' prefix:

```python
def decimal_to_binary(n):
    return bin(n)[2:]
```

This function works by converting the number to its binary representation using bin(), and then slicing off the first two characters to remove the '0b' prefix.

Both functions will give you the binary representation of a decimal number as a string with no leading zeros.

To verify the correctness of these functions, you can use the assert statement as follows:

```python
assert decimal_to_binary(8) == '1000'
```

This assertion will raise an AssertionError if the function does not correctly convert the number 8 to its binary representation '1000'.

Note that the decimal_to_binary() function can handle any positive integer as an argument, not just the number 8.

In general, assertions are used to check that a certain condition holds, and if it doesn't, an AssertionError is raised. They are particularly useful for checking the correctness of functions or algorithms.

In Python, you can use the assert keyword to define an assertion. The syntax is as follows:

```python
assert condition, error_message
```

If the condition is true, the assert statement does nothing. If the condition is