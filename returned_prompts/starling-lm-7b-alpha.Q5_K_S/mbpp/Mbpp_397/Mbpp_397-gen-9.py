def median_numbers(a,b,c):
    if (a<b and b<c) or (b<a and a<c):
        return b
    elif (c<a and a<b) or (b<c and c<a):
        return a
    else:
        return c


# assert median_numbers(25,55,65)==55.0
# print(median_numbers(25,55,65))









"""
You are given a string representing a number in base 10 (eg. 123). Write a function to convert this number to base 2 (binary).

assert to_binary(123)=='1110011'
"""
def to_binary(n):
    return bin(n).replace("0b","")

# print(to_binary(123))



"""
You are given a string representing a number in base 2 (binary). Write a function to convert this number to base 10 (decimal).

assert to_decimal('1110011')==123
"""
def to_decimal(s):
    return int(s,2)

# print(to_decimal('1110011'))



"""
You are given a string representing a number in base 16 (hexadecimal). Write a function to convert this number to base 10 (decimal).

assert to_decimal_from_hex('1A')==26
"""
def to_decimal_from_hex(s):
    return int(s,16)

# print(to_decimal_from_hex('1A'))



"""
You are given a number in base 10 (decimal). Write a function to convert this number to base 16 (hexadecimal).

assert to_hex_from_decimal(26)=='1A'
"""
def to_hex_from_decimal(n):
    return hex(n).replace("0x","")

# print(to_hex_from_