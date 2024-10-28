```
def decimal_to_binary(n):
    return bin(n)[2:]
```





This function uses Python's built-in `bin` function, which converts a decimal number to its binary equivalent. The `[2:]` is used to remove the '0b' prefix that `bin` adds to the output. For example, `bin(8)` would return `'0b1000'`, but `bin(8)[2:]` returns `'1000'`.