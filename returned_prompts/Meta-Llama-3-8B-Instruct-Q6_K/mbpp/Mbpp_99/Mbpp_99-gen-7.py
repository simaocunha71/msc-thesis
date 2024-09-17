```
def decimal_to_binary(n):
    return bin(n)[2:]
```
The function `decimal_to_binary` takes an integer `n` as input and returns its binary representation as a string.

The `bin` function in Python converts an integer to a binary string. However, it prefixes the binary string with `'0b'`. To get the binary string without the prefix, we use string slicing by indexing from the third character (`[2:]`).

For example, if we call `decimal_to_binary(8)`, it returns `'1000'`, which is the binary representation of the decimal number 8.