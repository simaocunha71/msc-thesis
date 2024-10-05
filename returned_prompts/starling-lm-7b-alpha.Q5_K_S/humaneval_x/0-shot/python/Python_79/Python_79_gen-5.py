
def decimal_to_binary(decimal):
    return "db{0:08b}db".format(decimal)


# Testing
print(decimal_to_binary(15))  # "db1111db"
print(decimal_to_binary(32))  # "db100000db"
print(decimal_to_binary(1))   # "db00000001db"
print(decimal_to_binary(1000))  # "db11001000db"





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
    return "db{0:08b}db".format(decimal)


# Testing
print(decimal_to_binary(15))  # "db1111db"
print(decimal_to_binary(32))  # "db100000db"
print(decimal_to_binary(1))   # "db00000001db"
print(decimal_to_binary(1000))  # "db11001000db"




def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of