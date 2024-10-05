
def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D']
    return sum(i in primes for i in num)

print(hex_key("AB"))  # 1
print(hex_key("1077E"))  # 2
print(hex_key("ABED1A33"))  # 4
print(hex_key("123456789ABCDEF0"))  # 6
print(hex_key("2020"))  # 2


# The function works by creating a list of the hexadecimal digits that are primes, 
# then it sums up the occurrences of these digits in the input string.
# The 'in' operator is used to check whether each character in the string is in the list of primes, 
# and the 'sum' function adds up these truth values (1 for each prime digit, 0 for each non-prime).
<jupyter_output>
1
2
4
6
2
<jupyter_text>
Exercise 5:
<jupyter_code>
