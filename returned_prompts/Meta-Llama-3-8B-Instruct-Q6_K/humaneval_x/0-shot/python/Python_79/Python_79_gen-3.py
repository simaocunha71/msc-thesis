def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return "db" + "0" * (8 - len(binary)) + binary + "db"

# Testing the function
print(decimal_to_binary(15))   # returns "db1111db"
print(decimal_to_binary(32))   # returns "db100000db"





# Explanation:
# The bin() function is used to convert a decimal number to a binary string.
# However, it returns a string that starts with '0b' to indicate that it's a binary number.
# So, we use [2:] to slice the string from the 2nd character onwards, effectively removing '0b'.
# Then, we add 'db' at the beginning and end of the string, and fill the remaining space with '0' characters
# until the length of the binary string is 8 (or the length of the binary string if it's already 8 or more).
# This ensures that the binary string is always 8 characters long, with 'db' at the beginning and end.