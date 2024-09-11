```
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    while len(binary) < 4:
        binary = '0' + binary
    return binary
```

Explanation:
The `decimal_to_binary` function takes a decimal number as input and uses Python's built-in `bin` function to convert it to its binary representation. However, the `bin` function prefixes the result with '0b', so we use `[2:]` to slice the string from the third character onwards to remove the prefix.

To ensure that the binary representation has no leading zeros, we use a while loop to prepend a '0' to the binary string until its length becomes four characters long. Finally, the function returns the binary string.

The assertion `assert decimal_to_binary(8) == '1000'` checks if the function correctly converts the decimal number 8 to its binary equivalent '1000'.

In this specific implementation, the function pads the binary string with leading zeros instead of truncating it. However, it is generally more efficient to truncate the binary string to the correct length instead of padding it.

A more efficient implementation of the `decimal_to_binary` function would be:

```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return binary if len(binary) >= 4 else '0' * (4 - len(binary)) + binary
```

This version of the function uses the same logic as the previous implementation, but instead of using a while loop to pad the binary string, it uses string concatenation to add the necessary number of leading zeros. This approach is more concise and avoids the overhead of the while loop.

Both versions of the function will produce the same result for the assertion `assert decimal_to_binary(8) == '1000'`.

Here's an example usage of the function:

```python
print(decimal_to_binary(8))  # Output: 1000
```

This will print the binary representation of the decimal number 8, which is '1000'.

