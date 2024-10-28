def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(3, 5))  # 1
print(gcd(25, 15))  # 5
