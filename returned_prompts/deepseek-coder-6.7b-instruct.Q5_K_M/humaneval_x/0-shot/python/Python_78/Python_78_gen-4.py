
def hex_key(num):
    prime_hex_digits = ['2', '3', '5', '7', 'B', 'D']
    return sum(hex_digit in prime_hex_digits for hex_digit in num)


print(hex_key("AB"))  # Output: 1
print(hex_key("1077E"))  # Output: 2
print(hex_key("ABED1A33"))  # Output: 4
print(hex_key("123456789ABCDEF0"))  # Output: 6
print(hex_key("2020"))  # Output: 2

# This function works by creating a list of prime hexadecimal digits and then uses the sum function to count how many times any hexadecimal digit in the input string is in the list of prime hexadecimal digits.
<jupyter_output>
1
2
4
6
2
<jupyter_text>
Question 3
<jupyter_code>
