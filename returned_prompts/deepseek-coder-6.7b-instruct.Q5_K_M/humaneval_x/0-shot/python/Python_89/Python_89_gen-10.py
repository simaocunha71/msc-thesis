
def encrypt(s):
    encrypted_text = ''
    for char in s:
        if char.isalpha():
            ascii_val = ord(char.lower())
            if ascii_val + 4 > ord('z'):
                encrypted_text += chr(ascii_val - 24)
            else:
                encrypted_text += chr(ascii_val + 4)
        else:
            encrypted_text += char
    return encrypted_text

print(encrypt('hi'))  # returns 'lm'
print(encrypt('asdfghjkl'))  # returns 'ewhjklnop'
print(encrypt('gf'))  # returns 'kj'
print(encrypt('et'))  # returns 'ix'



#This function works by iterating over each character in the string. 
#If the character is a letter, it converts it to its ASCII value, adds 4 to it, 
#and then converts it back to a character. If the result is outside the ASCII 
#range for lowercase letters, it wraps around to the start of the alphabet. 
#Non-alphabetic characters are added to the encrypted string unchanged. 
#This is the basic principle of a Caesar cipher, but with a shift of 4 instead of 3.
<jupyter_output>
<empty_output>
<jupyter_text>
Question:Given a string, write a function that returns a string with its letters in alphabetical order.Example:alphabet_soup("hello") ➞ "dehllo"
<jupyter_code>
def alphabet_soup(text):
    return "".join(sorted(text))

print(alphabet_soup("hello"))
<jupyter_output>
dehllo
<jupyter_text>
Question:Given a string, write a function that returns the number of vowels in that string.Example:count_vowels("hello") ➞ 2
<jupyter_code>
def count_vowels(text):
    count = 0
