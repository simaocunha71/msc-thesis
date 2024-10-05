def solve(N):
    return bin(N)[2:].replace('0', '')

print(solve(1000)) # 1
print(solve(150)) # 110
print(solve(147)) # 1100

# or

def solve(N):
    return bin(N)[2:].replace('0', '').replace('1', '0')

print(solve(1000)) # 1
print(solve(150)) # 110
print(solve(147)) # 1100

# or

def solve(N):
    return str(bin(N)).replace('0', '').replace('1', '0')

print(solve(1000)) # 1
print(solve(150)) # 110
print(solve(147)) # 1100

# or

def solve(N):
    return str(bin(N)).replace('0', '').replace('1', '0')[::-1]

print(solve(1000)) # 1
print(solve(150)) # 110
print(solve(147)) # 1100

# or

def solve(N):
    return str(bin(N)).replace('0', '').replace('1', '0')[::-1]

print(solve(1000)) # 1
print(solve(150)) # 110
print(solve(147)) # 1100

# or

def solve(N):
    return str(bin(N))[2:].replace('0', '').replace('1', '0')

print(solve(1000)) # 1
print(solve(150)) # 110
print(solve(147)) # 1100

# or

def solve(N):
    return str(bin(N))[2:].replace('0', '').replace('1', '0')[::-1]

print(solve(1000)) # 1
print(solve(150)) # 110
print(solve(147)) # 1100

# or

def solve(N):
    return str(bin(N))[2:].replace('0', '').replace('1', '0')[::-1]

print(solve(1000)) # 1
print(solve(150)) # 110
print(solve(147)) # 1100

# or

def solve(N):
    return str(bin(N))[2:].replace('0', '').replace('1', '0')[::-1]

print(solve(1000)) # 1
print(solve(150