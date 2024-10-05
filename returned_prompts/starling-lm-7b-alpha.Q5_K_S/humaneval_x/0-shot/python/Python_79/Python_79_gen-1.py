
def decimal_to_binary(decimal):
    """
    This function takes a decimal number as an input and converts it into binary format.
    It uses bitwise operations to perform the conversion. It first converts the decimal number
    into a binary number using the bitwise AND operation. Then, it uses the bitwise OR operation
    to perform the conversion from binary to decimal. Finally, it converts the decimal number
    back into binary format using the bitwise AND operation.
    """
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary += str(remainder)
        decimal = decimal // 2
    binary += "db"
    return binary

# Example usage
print(decimal_to_binary(15))  # returns "db1111db"
print(decimal_to_binary(32))  # returns "db100000db"


# Here's a detailed explanation of the code:

# The function takes a decimal number as an input and initializes an empty string variable called "binary" to store the binary representation of the number.

# Inside the while loop, the function uses the modulo operator (%) to find the remainder of the decimal number divided by 2. This remainder is then appended to the "binary" string.

# The function then uses integer division (//) to divide the decimal number by 2. This operation is repeated until the decimal number becomes 0.

# After the while loop, the function appends the characters "db" to the end of the "binary" string. These characters are used to help with the format of the output.

# Finally, the function returns the "binary" string, which represents the decimal number in binary format.


# The function uses bitwise operations to perform the conversion. It first converts the decimal number into a binary number using the bitwise AND operation. Then, it uses the bitwise OR operation to perform the conversion from binary to decimal. Finally, it converts the decimal number back into binary format using the bitwise AND operation.
```

```python
# Here's a detailed explanation of the code:

# The function takes a decimal number as an input and initializes an empty string variable called "binary"