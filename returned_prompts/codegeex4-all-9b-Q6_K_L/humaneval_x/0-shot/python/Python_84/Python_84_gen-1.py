def solve(N):
    return bin(N).count('1')

print(solve(1000))
print(solve(150))
print(solve(147))

# another solution
def solve(N):
    return bin(N)[2:].replace('0', '')

print(solve(1000))
print(solve(150))
print(solve(147))
