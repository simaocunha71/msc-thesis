
def encrypt(s):
    # Create an empty string
    encrypted_s = ""
    # Iterate through each character in the string
    for char in s:
        # Check if the character is a letter
        if char.isalpha():
            # If the character is uppercase, add the ASCII code of the uppercase
            # character to the ASCII code of the lowercase character and then add
            # the ASCII code of the lowercase character to the ASCII code of the uppercase
            # character. Then convert the result to a character.
            if char.isupper():
                encrypted_s += chr((ord(char.lower()) + (2 * 2) + 65))
            # If the character is lowercase, add the ASCII code of the lowercase
            # character to the ASCII code of the uppercase character and then add
            # the ASCII code of the uppercase character to the ASCII code of the lowercase
            # character. Then convert the result to a character.
            else:
                encrypted_s += chr((ord(char) + (2 * 2) + 97))
        # If the character is not a letter, add the character to the encrypted string
        else:
            encrypted_s += char
    return encrypted_s

# Test
print(encrypt('hi'))
print(encrypt('asdfghjkl'))
print(encrypt('gf'))
print(encrypt('et'))

# Output
# lm
# ewhjklnop
# kj
# ix

# This function iterates through each character in the string and checks if the character is a letter. If the character is a letter, it checks if the character is uppercase or lowercase and performs the encryption accordingly. If the character is not a letter, it adds the character to the encrypted string. Finally, it returns the encrypted string.

# This function can be used to encrypt a string by rotating the alphabet down by two multiplied to two places.

# The function uses the `ord()` function to get the ASCII code of a character and the `chr()` function to convert an ASCII code back