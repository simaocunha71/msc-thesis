```
def decimal_to_binary(n):
    return bin(n)[2:]
```
The unit test `assert decimal_to_binary(8) == '1000'` suggests that the function should return a string with no leading zeros. The built-in `bin()` function in Python converts an integer to a binary string, but it adds a '0b' prefix. We can use string slicing to remove this prefix, so `bin(n)[2:]` is used to get the binary representation as a string without leading zeros. This function works correctly for positive integers. If you need to handle negative integers, you can add a check at the beginning of the function to convert them to positive before performing the conversion. Here's how you can do it:

```
def decimal_to_binary(n):
    if n < 0:
        n = n * -1
    return bin(n)[2:]
```
This function will work correctly for both positive and negative integers, and it will return the binary representation as a string without leading zeros. 