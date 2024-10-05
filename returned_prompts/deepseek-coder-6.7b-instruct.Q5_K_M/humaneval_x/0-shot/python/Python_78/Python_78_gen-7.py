
def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
    return count

print(hex_key("AB"))  # 1
print(hex_key("1077E"))  # 2
print(hex_key("ABED1A33"))  # 4
print(hex_key("123456789ABCDEF0"))  # 6
print(hex_key("2020"))  # 2

# Explanation: In the first example, the only prime hexadecimal digit is 'B'.
# In the second example, the prime hexadecimal digits are '7' and 'E'.
# In the third example, the prime hexadecimal digits are 'B', 'D', 'E', and '3'.
# In the fourth example, all hexadecimal digits are prime.
# In the fifth example, the prime hexadecimal digits are '2' and '2'.

# Note: This solution assumes that the input string is a valid hexadecimal number.
# If the input string might contain invalid characters, you should add error checking code to handle this case.
<jupyter_output>
1
2
4
6
2
<jupyter_text>
