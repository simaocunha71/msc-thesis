def solve(N):
    return bin(N)[2:]

print(solve(1000)) # 1
print(solve(150)) # 110
print(solve(147)) # 1100

Explanation:
The bin() function returns the binary string of a number. The [2:] slice removes the "0b" prefix from the binary string.