```
def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            result += chr((ord(char) - ascii_offset + 4 * 2) % 26 + ascii_offset)
        else:
            result += char
    return result
```

This function iterates over each character in the input string. If the character is a letter, it calculates the new character by shifting the ASCII value of the original character down by 4 times 2 (8) places. It uses the modulus operator to ensure that the shift wraps around the alphabet if necessary. If the character is not a letter, it simply adds it to the result string as is. The function returns the encrypted string.