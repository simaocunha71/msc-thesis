def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

assert decimal_to_binary(8) == '1000'
assert decimal_to_binary(0) == '0'
assert decimal_to_binary(1) == '1'
assert decimal_to_binary(16) == '10000'
assert decimal_to_binary(255) == '11111111'

"""
Explanation:
This function works by dividing the decimal number by 2, and storing the remainder as the next digit in the binary number. It continues this process until the decimal number becomes 0. The binary number is then returned as a string.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Exercise 3
<jupyter_code>
