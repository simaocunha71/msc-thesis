```
def solve(N):
    bin_str = bin(N)[2:]  # Convert N to binary and remove '0b' prefix
    return ''.join('1' for digit in bin_str)  # Count the number of '1's and return as a string
```







Solution:
```
def solve(N):
    bin_str = bin(N)[2:]  # Convert N to binary and remove '0b' prefix
    return ''.join('1' for digit in bin_str)  # Count the number of '1's and return as a string
```







Explanation:
The function `solve(N)` takes a positive integer `N` as input and returns the total sum of its digits in binary as a string.

Here's how it works:
1. `bin(N)[2:]` is used to convert the integer `N` to a binary string and remove the '0b' prefix.
2. `''.join('1' for digit in bin_str)` is used to count the number of '1's in the binary string and return it as a string.

For example, if `N` is 1000, the binary string would be '11000000000'. The function would count the number of '1's (which is 1) and return '1'.

Note: The constraints of the problem are 0 ≤ N ≤ 10000, which means the function will only be called with integers within this range.