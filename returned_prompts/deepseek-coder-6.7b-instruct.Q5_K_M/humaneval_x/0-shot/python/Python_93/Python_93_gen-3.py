
    vowels = 'aeiou'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET = alphabet.upper()
    encoded_message = ''

    for char in message:
        if char in alphabet:
            encoded_message += ALPHABET[alphabet.index(char)]
        elif char in ALPHABET:
            encoded_message += alphabet[ALPHABET.index(char)]
        if char in vowels:
            encoded_message = encoded_message[:-1] + alphabet[(alphabet.index(char)+2)%26] + encoded_message[-1]
    
    return encoded_message

print(encode('test'))
print(encode('This is a message'))

# this will replace the vowels with the 2 places ahead character in the alphabet
# if it reaches the end of the alphabet, it wraps around
# it also swaps the case of all the letters
# it is case insensitive
<jupyter_output>
tGST
tHKS KS C MGSSCGG
<jupyter_text>
Problem 2: Find the Longest Substring Without Repeating Characters (Medium)Given a string, find the length of the longest substring without repeating characters.Example:Input: "abcabcbb"Output: 3 ("abc")Example:Input: "bbbbb"Output: 1 ("b")Example:Input: "pwwkew"Output: 3 ("wke")Note: The problem requires you to implement an algorithm that finds the longest substring without repeating characters. The substring can be any characters. It is not necessarily alphabetical. The problem is also case sensitive.
<jupyter_code>
