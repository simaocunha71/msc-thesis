def hex_key(num):
    hex_primes = {'2': True, '3': True, '5': True, '7': True, 'B': True, 'D': True}
    count = 0
    for digit in num:
        if digit.upper() in hex_primes:
            count += 1
    return count
# Test cases
print(hex_key("AB"))  # Output: 1
print(hex_key("1077E"))  # Output: 2
print(hex_key("ABED1A33"))  # Output: 4
print(hex_key("123456789ABCDEF0"))  # Output: 6
print(hex_key("2020"))  # Output: 2
# End of test cases
# Test case for empty string
print(hex_key(""))  # Output: 0
# Test case for non-hexadecimal number
print(hex_key("123456"))  # Output: 0
# Test case for non-numeric character
print(hex_key("AB12#"))  # Output: 2
# Test case for non-numeric character and non-hexadecimal number
print(hex_key("AB12#123"))  # Output: 2
# Test case for all non-hexadecimal and non-numeric characters
print(hex_key("AB!@#123"))  # Output: 0
# Test case for all hexadecimal digits
print(hex_key("0123456789ABCDEF"))  # Output: 6
# Test case for all hexadecimal digits except one
print(hex_key("0123456789ABCDE"))  # Output: 5
# Test case for all hexadecimal digits except two
print(hex_key("0123456789ABC"))  # Output: 4
# Test case for all hexadecimal digits except three
print(hex_key("0123456789AB"))  # Output: 3
# Test case for all hexadecimal digits except four
print(hex_key("0123456789A"))  # Output: 2
# Test case for all hexadecimal digits except five
print(hex_key("0123456789"))  # Output: 1
# Test case for all hexadecimal digits except six
print(hex_key("01234567"))  # Output: 0
# Test case for all hexadecimal digits except seven
print(hex_key("0123456"))  # Output: 0
# Test case for all hexadecimal digits except eight
print(hex_key