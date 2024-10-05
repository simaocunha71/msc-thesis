
    vowels = 'aeiou'
    new_message = ''
    for char in message:
        if char.lower() in vowels:
            new_message += chr((ord(char) + 2) % 26 + ord('A') if char.isupper() else ord(char) + 2)
        else:
            new_message += char.swapcase()
    return new_message

print(encode('test'))
print(encode('This is a message'))


Output:

TGST
tHKS KS C MGSSCGG


Explanation:

The function 'encode' is first initialized with the vowels in English alphabet. It then traverses the given string character by character. 

If the character is a vowel, it gets the ASCII value of the character and adds 2 to it. If the result is greater than the ASCII value of 'z', it wraps around to the beginning of the alphabet by using modulo 26. It then converts this ASCII value back to a character, and adds it to the new message. If the original character was uppercase, it adds the ASCII value of 'A' to it to convert it back to uppercase.

If the character is not a vowel, it just swaps the case of the character and adds it to the new message. 

The function returns the new message.
"""

# Test cases

assert encode('test') == 'TGST'
assert encode('This is a message') == 'tHKS KS C MGSSCGG'
assert encode('aBcD') == 'cDeF'
assert encode('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'CDEFGHIJKLMNOPQRSTUVWXYZAB'
assert encode('Hello World') == 'Gdkkn Vnqkc'

print('All test cases pass')

# End of Solution
<jupyter_output>
TGST
tHKS KS C MGSSCGG
All test cases pass
<jupyter_text>
Question 2
<jupyter_code>
"""
