Here is the Python solution to the problem:

```python
def odd_Equivalent(binary, rotations):
    n = len(binary)
    binary = binary + binary
    binary = list(binary)
    odd_count = 0
    for i in range(len(binary) // 2):
        binary[i] = int(binary[i])
        binary[i+n] = int(binary[i+n])
    for _ in range(rotations):
        for i in range(n):
            binary[i+n] = binary[i] ^ binary[i+1]
        binary[-1] = binary[0] ^ binary[1]
        for i in range(n):
            if binary[i] % 2 == 1:
                odd_count += 1
    return odd_count

assert odd_Equivalent("011001",6) == 3
```

In the above code, the function `odd_Equivalent()` takes two parameters `binary` and `rotations`. It first converts the binary string to a list of integers and then rotates the binary string `rotations` times and keeps a count of how many times the binary representation of a number is odd. The function finally returns this count.

The rotation is performed by XORing the current bit with the next bit and storing the result. This is repeated `n` times where `n` is the length of the binary string. Then XORing the last bit with the first bit is performed and the result is stored. The count of odd numbers is then incremented if the binary representation of the number is odd. This process is repeated for `rotations` times.

Finally, the function returns the count of numbers for which the binary representation is odd after all rotations.
"""

assert odd_Equivalent("011001",6) == 3
"""
assert odd_Equivalent("011001",6) == 3
The binary representation of 1 (01) after rotating 6 times is 10. The binary representation of 2 (10) after rotating 6 times is 10. The binary representation of 5 (101) after rotating 6 times is 10. All of these have an odd value, so