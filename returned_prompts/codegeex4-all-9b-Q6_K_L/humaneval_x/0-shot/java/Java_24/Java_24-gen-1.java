def largestDivisor(n):
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return n

print(largestDivisor(15)) # 5

def largestDivisor(n):
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return n

print(largestDivisor(15)) # 5