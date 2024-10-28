
def decimal_to_binary(decimal):
    binary = '{0:b}'.format(decimal)
    return 'db' + binary + 'db'



# Test Cases
print(decimal_to_binary(15))    # Returns "db1111db"
print(decimal_to_binary(32))    # Returns "db100000db"
print(decimal_to_binary(2))     # Returns "db10db"
print(decimal_to_binary(0))     # Returns "db0db"
print(decimal_to_binary(500))   # Returns "db11001000db"




# Other Solutions

def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """

    return 'db' + '{0:b}'.format(decimal) + 'db'



# Test Cases
print(decimal_to_binary(15))    # Returns "db1111db"
print(decimal_to_binary(32))    # Returns "db100000db"
print(decimal_to_binary(2))     # Returns "db10db"
print(decimal_to_binary(0))     # Returns "db0db"
print(decimal_to_binary(500))   # Returns "db11001000db"


```
