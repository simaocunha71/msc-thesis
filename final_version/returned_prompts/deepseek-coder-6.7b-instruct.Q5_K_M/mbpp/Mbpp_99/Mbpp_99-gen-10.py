def decimal_to_binary(n):
    return bin(n).replace("0b", "")

print(decimal_to_binary(8))

"""
Explanation:
The built-in python function bin() converts the decimal number to binary. The "0b" that is automatically added to the binary string is removed with the replace() function.
"""

"""
Test Cases:
assert decimal_to_binary(0) == '0'
assert decimal_to_binary(1) == '1'
assert decimal_to_binary(2) == '10'
assert decimal_to_binary(3) == '11'
assert decimal_to_binary(10) == '1010'
assert decimal_to_binary(16) == '10000'
assert decimal_to_binary(255) == '11111111'
assert decimal_to_binary(1023) == '1111111111'
"""

"""
Test Cases:
assert decimal_to_binary(0) == '0'
assert decimal_to_binary(1) == '1'
assert decimal_to_binary(2) == '10'
assert decimal_to_binary(3) == '11'
assert decimal_to_binary(10) == '1010'
assert decimal_to_binary(16) == '10000'
assert decimal_to_binary(255) == '11111111'
assert decimal_to_binary(1023) == '1111111111'
"""
<jupyter_output>
1000
<jupyter_text>
Problem 3: Anagram Checker
<jupyter_code>
