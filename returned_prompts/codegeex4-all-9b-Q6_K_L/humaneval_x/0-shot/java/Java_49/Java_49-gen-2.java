def modp(n, p):
    return pow(2, n, p)

print(modp(3, 5))
print(modp(1101, 101))
print(modp(0, 101))
print(modp(3, 11))
print(modp(100, 101))