```
def decimal_to_binary(n):
    return bin(n)[2:]
```
This function uses Python's built-in `bin` function to convert the decimal number to a binary string. The `[2:]` is used to remove the '0b' prefix that `bin` adds to the output. 

For example, `bin(8)` would return '0b1000', so `[2:]` removes the '0b' to leave '1000'. 

This function should pass the given unit test: `assert decimal_to_binary(8) == '1000'`. 

Note that this function assumes that the input is a non-negative integer. If the input can be negative or a non-integer, additional error handling would be needed. 