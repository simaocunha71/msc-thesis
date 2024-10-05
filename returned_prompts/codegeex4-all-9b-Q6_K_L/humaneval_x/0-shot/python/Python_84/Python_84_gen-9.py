def solve(N):
    return bin(N).replace('0b', '')

print(solve(1000)) # 1
print(solve(150)) # 110
print(solve(147)) # 1100