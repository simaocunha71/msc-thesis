```
def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + 2*2) % 26 + ascii_offset)
        else:
            result += char
    return result
```


Example usage:
```
print(encrypt('hi'))  # Output: lm
print(encrypt('asdfghjkl'))  # Output: ewhjklnop
print(encrypt('gf'))  # Output: kj
print(encrypt('et'))  # Output: ix
```


Explanation:
The function `encrypt` takes a string `s` as an argument and returns an encrypted string. It iterates over each character in the string. If the character is a letter (checked using `isalpha()`), it calculates the encrypted character by shifting the ASCII value of the character down by 2 multiplied by 2 places. The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to convert the ASCII value back to a character. The `ascii_offset` variable is used to handle uppercase and lowercase letters correctly. If the character is not a letter, it is left unchanged. The encrypted string is then returned.