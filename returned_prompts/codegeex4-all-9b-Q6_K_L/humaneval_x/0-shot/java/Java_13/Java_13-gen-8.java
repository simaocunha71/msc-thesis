def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def greatestCommonDivisor(a, b):
    return gcd(a, b)

print(greatestCommonDivisor(3, 5))  # 1
print(greatestCommonDivisor(25, 15))  # 5

