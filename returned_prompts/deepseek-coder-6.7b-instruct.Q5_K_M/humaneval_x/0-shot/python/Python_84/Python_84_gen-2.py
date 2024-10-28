
def solve(N):
    binary_N = bin(N)[2:]
    sum_of_digits = sum(int(digit) for digit in binary_N)
    return bin(sum_of_digits)[2:]

print(solve(1000)) # "1"
print(solve(150))  # "110"
print(solve(147))  # "1100"

# ------
# Solution 2:

def solve(N):
    return bin(sum(map(int, str(bin(N)[2:]))))[2:]

print(solve(1000)) # "1"
print(solve(150))  # "110"
print(solve(147))  # "1100"

# ------
# Solution 3:

def solve(N):
    return bin(sum(int(d) for d in bin(N)[2:]))[2:]

print(solve(1000)) # "1"
print(solve(150))  # "110"
print(solve(147))  # "1100"

# ------
# Solution 4:

def solve(N):
    binary_N = bin(N)[2:]
    return bin(sum(int(digit) for digit in binary_N))[2:]

print(solve(1000)) # "1"
print(solve(150))  # "110"
print(solve(147))  # "1100"

# ------
# Solution 5:

def solve(N):
    return bin(sum(int(i) for i in bin(N)[2:]))[2:]

print(solve(1000)) # "1"
print(solve(150))  # "110"
print(solve(147))  # "1100"

# ------
# Solution 6:

def