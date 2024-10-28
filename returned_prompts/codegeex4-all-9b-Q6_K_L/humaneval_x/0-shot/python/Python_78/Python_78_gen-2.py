def hex_key(num):
    primes = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for c in num if c in primes)

print(hex_key("AB"))  # 1
print(hex_key("1077E"))  # 2
print(hex_key("ABED1A33"))  # 4
print(hex_key("123456789ABCDEF0"))  # 6
print(hex_key("2020"))  # 2