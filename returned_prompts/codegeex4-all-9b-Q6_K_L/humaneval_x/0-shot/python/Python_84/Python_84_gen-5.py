def solve(N):
    return bin(N)[2:].count('1')

print(solve(1000))
print(solve(150))
print(solve(147))