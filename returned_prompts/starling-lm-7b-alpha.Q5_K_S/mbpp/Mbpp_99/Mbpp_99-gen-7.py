```
def decimal_to_binary(n):
    s = ""
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    return s
```

This function takes a decimal number as input and converts it into its binary equivalent represented as a string with no leading zeros. It does this by repeatedly dividing the input number by 2 and concatenating the remainder (0 or 1) at the beginning of the string. The process continues until the input number becomes 0.

To test the function, you can use the assertion provided in the question. The assertion checks if the function correctly converts the decimal number 8 to its binary equivalent, which should be the string '1000'.

You can run the function with different decimal numbers to see if it correctly converts them to binary equivalents. For example, if you call `decimal_to_binary(10)`, it should return the string '1010', which is the binary representation of 10.

Overall, this function provides a concise and efficient way to convert decimal numbers to binary equivalents in Python.

```python
def decimal_to_binary(n):
    s = ""
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    return s
```

This Python function takes a decimal number as input and converts it into its binary equivalent represented as a string with no leading zeros. It uses a while loop to repeatedly divide the input number by 2 and concatenate the remainder (0 or 1) at the beginning of the string. The process continues until the input number becomes 0. The function returns the binary string as the result.

To test the function, you can use the provided assertion `assert decimal_to_binary(8) == '1000'`. This assertion checks if the function correctly converts the decimal number 8 to its binary equivalent, which should be the string '1000'.

You can run the function with different decimal numbers to see if it correctly converts them to binary equivalents. For example, if you call `decimal_to_binary(10)`, it should return the string '1