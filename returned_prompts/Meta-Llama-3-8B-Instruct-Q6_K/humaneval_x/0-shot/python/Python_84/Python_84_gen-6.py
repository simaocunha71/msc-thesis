```
def solve(N):
    return bin(N).replace("0b", "")  # Convert to binary and remove the "0b" prefix
```


This function takes an integer N as input and returns the binary representation of N as a string. It does this by using the built-in Python function `bin()`, which converts an integer to a binary string. The `replace()` method is then used to remove the "0b" prefix that `bin()` adds to the output. The result is a string that is the binary representation of the input integer.