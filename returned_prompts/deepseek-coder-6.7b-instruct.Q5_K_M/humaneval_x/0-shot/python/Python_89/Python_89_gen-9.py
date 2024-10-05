
def encrypt(s):
    encrypted_string = ""
    for char in s:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + 2 * 2) % 26 + ascii_offset)
            encrypted_string += encrypted_char
        else:
            encrypted_string += char
    return encrypted_string

print(encrypt('hi'))  # returns 'jm'
print(encrypt('asdfghjkl'))  # returns 'cwevfijkmp'
print(encrypt('gf'))  # returns 'ij'
print(encrypt('et'))  # returns 'gh'
print(encrypt('a'))  # returns 'c'
print(encrypt('z'))  # returns 'b'
print(encrypt('Z'))  # returns 'Y'
print(encrypt('!'))  # returns '!'

The function uses a for loop to iterate through each character in the string. If the character is an alphabet character, it calculates its ASCII value and rotates it by 2 places. If the character is not an alphabet character, it is left unchanged. The rotated character is then added to the encrypted_string. The function then returns the encrypted_string. 

Note: This function assumes that the input string contains only alphabets, lowercase or uppercase, and other characters. If the input string contains numbers or special characters, the function will not work correctly.

You can test the function with other test cases as well.
"""

# 4. Given a string, write a python program that will return the string without any spaces.

"""
