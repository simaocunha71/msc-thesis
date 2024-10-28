
def hex_key(num):
    primes = {'2', '3', '5', '7', 'B', 'D'}
    return sum(c in primes for c in num)

print(hex_key("AB"))  # 1
print(hex_key("1077E"))  # 2
print(hex_key("ABED1A33"))  # 4
print(hex_key("123456789ABCDEF0"))  # 6
print(hex_key("2020"))  # 2


"""
Explanation:

The function hex_key takes a string num as input. It defines a set of hexadecimal digits that are primes. 
The sum function is called with the generator expression (c in primes for c in num), which creates a sequence of 1's and 0's, 
where 1 indicates that a hexadecimal digit is prime and 0 indicates that it is not. The sum function then returns the total count 
of these 1's, which is the number of prime digits in the input string.
"""

"""
This solution works by utilizing the built-in set data structure in python. This allows for efficient membership tests, 
which are used to count the number of prime hexadecimal digits in the input string.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 5
<jupyter_code>
