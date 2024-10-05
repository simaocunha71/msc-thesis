```
def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + 2 * 2) % 26 + ascii_offset)
        else:
            result += char
    return result
```


The function `encrypt(s)` takes a string `s` as an argument and returns the encrypted string. 

It iterates over each character in the string. If the character is a letter, it calculates the new character by shifting the original character's ASCII value down by 4 places (2 * 2). It handles both uppercase and lowercase letters by adjusting the ASCII offset accordingly. If the character is not a letter, it leaves it unchanged. 

Finally, it returns the encrypted string. 

For example, the string 'hi' is encrypted to 'lm', 'asdfghjkl' is encrypted to 'ewhjklnop', and so on. 







