def hex_key(num):
    return sum(d in '2357BD' for d in num)

print(hex_key('AB'))  # 1
print(hex_key('1077E'))  # 2
print(hex_key('ABED1A33'))  # 4
print(hex_key('123456789ABCDEF0'))  # 6
print(hex_key('2020'))  # 2