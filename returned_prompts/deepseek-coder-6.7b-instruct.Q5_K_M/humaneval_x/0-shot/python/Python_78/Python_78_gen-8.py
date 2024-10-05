
def hex_key(num):
    prime_hex_digits = ['2', '3', '5', '7', 'B', 'D']
    return sum(1 for ch in num if ch in prime_hex_digits)

print(hex_key("AB"))  # 1
print(hex_key("1077E"))  # 2
print(hex_key("ABED1A33"))  # 4
print(hex_key("123456789ABCDEF0"))  # 6
print(hex_key("2020"))  # 2


# Alternate solution using list comprehension and count method

def hex_key(num):
    prime_hex_digits = ['2', '3', '5', '7', 'B', 'D']
    return len([ch for ch in num if ch in prime_hex_digits])

print(hex_key("AB"))  # 1
print(hex_key("1077E"))  # 2
print(hex_key("ABED1A33"))  # 4
print(hex_key("123456789ABCDEF0"))  # 6
print(hex_key("2020"))  # 2

# Another alternate solution using map function and count method

def hex_key(num):
    prime_hex_digits = ['2', '3', '5', '7', 'B', 'D']
    return sum(map(num.count, prime_hex_digits))

print(hex_key("AB"))  # 1
print(hex_key("1077E"))  # 2
print(hex_key("ABED1A33"))  # 4
print(hex_key("123456789ABCDEF0"))  # 6
print(hex_key("2020"))  # 2

# Another alternate solution using issubset method

def hex_key(num):
    prime_hex_digits = ['2', '3', '5', '7', 'B', 'D']
    return sum(