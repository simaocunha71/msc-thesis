
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    binary_str = 'db' + binary + 'db'
    return binary_str

print(decimal_to_binary(15))  # returns  "db1111db"
print(decimal_to_binary(32))  # returns  "db100000db"

# Here, the function bin() is used to convert the decimal number to binary. The [2:] slice is used to remove the '0b' prefix that Python adds to binary numbers. The 'db' prefix and suffix are then added using string concatenation.



# Another solution using while loop:

def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return 'db' + binary + 'db'

print(decimal_to_binary(15))  # returns  "db1111db"
print(decimal_to_binary(32))  # returns  "db100000db"

# This solution uses a while loop to repeatedly divide the decimal by 2 and add the remainder to the start of the binary string. The loop continues until the decimal is 0. The 'db' prefix and suffix are then added using string concatenation.
<jupyter_output>
db1111db
db100000db
<jupyter_text>
Question 2:Write a function in python that can find all the even numbers in a list.
<jupyter_code>
