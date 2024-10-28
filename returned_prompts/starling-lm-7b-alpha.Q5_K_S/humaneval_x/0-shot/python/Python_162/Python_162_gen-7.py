
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    """

    import hashlib

    if text == '':
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()

# Test
print(string_to_md5('Hello world'))  # Output: '3e25960a79dbc69b674cd4ec67a72c62'



# Using hashlib to compute the md5 hash
# https://docs.python.org/3/library/hashlib.html#hashlib.md5

# Import the hashlib module
# https://docs.python.org/3/library/hashlib.html

# Compute the md5 hash of the input string
# https://docs.python.org/3/library/hashlib.html#hashlib.md5.hexdigest

# Convert the md5 hash to a hexadecimal string
# https://docs.python.org/3/library/stdtypes.html#str.hex

# Return the md5 hash as a string


# If the input string is an empty string, return None


# Test

# Verify the md5 hash of the string 'Hello world'
print(string_to_md5('Hello world'))
# Output: '3e25960a79dbc69b674cd4ec67a72c62'

# Test

# Verify the md5 hash of the string ''
print(string_to_md5(''))
# Output: None







































































































