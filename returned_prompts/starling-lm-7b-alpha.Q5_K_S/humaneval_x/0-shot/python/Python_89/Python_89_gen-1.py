
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    encrypted_str = ""
    for char in s:
        char_code = ord(char)
        if char_code >= 65 and char_code <= 90:
            encrypted_str += chr(((char_code - 65 + 2 * 2) % 26) + 65)
        elif char_code >= 97 and char_code <= 122:
            encrypted_str += chr(((char_code - 97 + 2 * 2) % 26) + 97)
        else:
            encrypted_str += char
    return encrypted_str

# Testing
print(encrypt('hi')) # lm
print(encrypt('asdfghjkl')) # ewhjklnop
print(encrypt('gf')) # kj
print(encrypt('et')) # ix















































































































































































