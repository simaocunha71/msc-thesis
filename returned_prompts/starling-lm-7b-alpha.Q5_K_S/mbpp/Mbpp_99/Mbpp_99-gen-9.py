```
def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary_number = ''
    while n > 0:
        binary_number = str(n % 2) + binary_number
        n //= 2
    return binary_number
```

Here's a Python function that takes a decimal number as input and returns its binary equivalent as a string with no leading zeros. The function works by repeatedly dividing the number by 2 and appending the remainder (0 or 1) to the left of the binary number string until the original number becomes zero.

For example, if we call `decimal_to_binary(8)`, the function will perform the following steps:

1. Check if the input number is zero. If it is, return the string '0' as the binary equivalent.
2. Initialize an empty string `binary_number` to store the binary representation of the number.
3. Enter a loop that continues until the number becomes zero.
4. Inside the loop, calculate the remainder of the number divided by 2 using the modulo operator `%`. This gives us the rightmost digit of the binary representation.
5. Convert the remainder to a string and concatenate it to the left of the `binary_number` string. This ensures that the binary representation is built up from left to right.
6. Update the number by performing integer division (`n //= 2`) to move on to the next digit in the binary representation.
7. Repeat steps 4-6 until the number becomes zero, at which point the binary representation is complete.
8. Return the `binary_number` string, which now holds the binary equivalent of the original decimal number.

In the case of `decimal_to_binary(8)`, the function will return the string '1000' as the binary representation of 8.

This implementation ensures that the binary representation is built up from left to right with no leading zeros, as specified in the problem statement.

You can test the function with other decimal numbers to verify its correctness and see how it converts them to binary.

```python
print(decimal_to_binary(10))  # Output: '1010'
print(decimal_