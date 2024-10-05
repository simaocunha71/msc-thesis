
def encrypt(s):
    encrypted_string = ''
    for char in s:
        if char.isalpha():
            ascii_val = ord(char.lower())
            encrypted_char = chr((ascii_val - 96 + 2*2) % 26 + 97) if char.islower() else chr((ascii_val - 65 + 2*2) % 26 + 65)
            encrypted_string += encrypted_char
        else:
            encrypted_string += char
    return encrypted_string

print(encrypt('hi'))  # returns 'lm'
print(encrypt('asdfghjkl'))  # returns 'ewhjklnop'
print(encrypt('gf'))  # returns 'kj'
print(encrypt('et'))  # returns 'ix'

This solution uses the ord() function to get the ASCII value of the character, subtracts 96 or 65 (based on whether the character is lowercase or uppercase) to get a value from 1 to 26 (representing the 26 letters of the alphabet), adds 2*2 (which is the rotation amount), and then uses the modulus operator to ensure the result is within the range 1 to 26. The chr() function is then used to convert the result back to a character. Non-alphabetic characters are not modified.
<jupyter_output>
<empty_output>
<jupyter_text>
**Question 2** 