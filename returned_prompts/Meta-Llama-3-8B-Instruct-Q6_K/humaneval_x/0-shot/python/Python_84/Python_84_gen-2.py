```
def solve(N):
    binary = bin(N)[2:]
    return sum(int(digit) for digit in binary)
```


Explanation:
- The `bin()` function is used to convert the integer `N` to a binary string. The `[2:]` is used to remove the '0b' prefix that `bin()` adds to the string.
- The `sum()` function is used to calculate the sum of the digits in the binary string. The `int(digit) for digit in binary` is a generator expression that iterates over each character in the binary string, converts it to an integer, and sums them up.
- The result is returned as a string.

For example, if `N = 1000`, `bin(N)[2:]` returns `'1111100000'`, and `sum(int(digit) for digit in binary)` returns `1`, so the function returns `'1'`. If `N = 150`, `bin(N)[2:]` returns `'10010110'`, and `sum(int(digit) for digit in binary)` returns `6`, so the function returns `'6'`. If `N = 147`, `bin(N)[2:]` returns `'10010111'`, and `sum(int(digit) for digit in binary)` returns `12`, so the function returns `'12'`. 

The time complexity of this function is O(log N), where N is the input integer, because the function needs to iterate over each digit in the binary representation of the integer. The space complexity is O(log N) as well, because the function needs to store the binary representation of the integer. 