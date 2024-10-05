def solve(N):
    return bin(N)[2:].count('1')

print solve(1000)
print solve(150)
print solve(147)

This will first convert the number to binary using the built-in Python function bin. The bin function returns a string that starts with '0b' and then the binary representation of the number. We want to ignore the '0b' part, so we slice the string from index 2 to the end. Then we count the number of '1's in the resulting string using the count method.