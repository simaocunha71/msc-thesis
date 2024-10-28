def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    binary = "db" + binary + "db"
    return binary

print(decimal_to_binary(15))   # returns "db1111db"
print(decimal_to_binary(32))   # returns "db100000db"





# Binary numbers are represented as strings of '0's and '1's. You can convert decimal numbers to binary using the bin() function in Python, which returns a string that starts with '0b'. We remove the '0b' by using [2:].

# We then add 'db' at the beginning and at the end of the binary string to match the format. 

# The bin() function is a built-in function in Python that converts an integer number to a binary string. The binary string always starts with '0b' to indicate that it is a binary number. We use [2:] to remove the '0b' from the binary string.