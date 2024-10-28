```
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[2*2:] + alphabet[:2*2]
    result = ''
    for char in s:
        if char.isalpha():
            if char.islower():
                result += shifted_alphabet[alphabet.index(char)]
            else:
                result += shifted_alphabet[alphabet.index(char.lower())].upper()
        else:
            result += char
    return result
```


The function encrypt takes a string as an argument and returns the encrypted string. It first creates the shifted alphabet by concatenating the last two times the shift amount characters from the end of the original alphabet to the first two times the shift amount characters from the start of the original alphabet.

Then it iterates over each character in the input string. If the character is a letter, it finds the index of the character in the original alphabet, uses that index to get the corresponding character in the shifted alphabet, and adds it to the result string. If the character is not a letter, it simply adds the character to the result string.

Finally, it returns the encrypted string. The function handles both lowercase and uppercase letters, and leaves non-letter characters unchanged.