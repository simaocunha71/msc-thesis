```
def decimal_to_binary(n):
    return bin(n)[2:]
```
The problem is asking to write a function that converts a given decimal number to its binary equivalent and returns it as a string. The binary string should not have any leading zeros.

The unit test `assert decimal_to_binary(8) == '1000'` helps to clarify the problem by showing that the binary string should not have any leading zeros.

The solution uses the built-in `bin` function in Python, which converts an integer to a binary string. The `[2:]` is used to remove the first two characters of the binary string, which are '0b', the prefix that `bin` adds to the string. This ensures that the binary string does not have any leading zeros. For example, `bin(8)` returns '0b1000', and `bin(8)[2:]` returns '1000'. 

Here is the full code:
```
def decimal_to_binary(n):
    return bin(n)[2:]
``` 







