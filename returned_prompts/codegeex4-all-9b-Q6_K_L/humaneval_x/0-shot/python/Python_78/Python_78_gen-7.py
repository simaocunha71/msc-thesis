def hex_key(num):
    primes = {'2','3','5','7','B','D'}
    return sum([1 for c in num if c in primes])

print(hex_key("AB"))
print(hex_key("1077E"))
print(hex_key("ABED1A33"))
print(hex_key("123456789ABCDEF0"))
print(hex_key("2020"))

This code works by iterating over each character in the string and checking if it is in the set of prime hexadecimal digits. If it is, it adds 1 to the count. The sum() function is then used to sum up all the 1s, giving the total number of prime hexadecimal digits in the string.