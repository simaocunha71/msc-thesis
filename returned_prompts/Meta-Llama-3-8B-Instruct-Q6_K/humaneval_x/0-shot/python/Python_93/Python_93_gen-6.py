Here is the Python code to solve the problem:

```Python
def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in message:
        if char in vowels:
            index = vowels.index(char)
            if char.isupper():
                result += chr((index + 2) % 26 + ord('A'))
            else:
                result += chr((index + 2) % 26 + ord('a'))
        elif char.isalpha():
            if char.isupper():
                result += chr(ord(char) + 32)
            else:
                result += chr(ord(char) - 32)
        else:
            result += char
    return result
```

This function goes through each character in the message. If the character is a vowel, it finds the index of the vowel in the string 'aeiouAEIOU', adds 2 to the index, and converts the resulting code to a character. If the original vowel was uppercase, it converts the new character to uppercase. If the character is not a vowel, it converts it to the opposite case. If the character is not a letter, it leaves it as is. The function then returns the encoded message.  The `% 26` is used to ensure that the index wraps around the alphabet if it goes past 'z' or 'Z'. The `ord` function is used to convert the characters to their ASCII codes, and `chr` is used to convert the ASCII codes back to characters. The `isalpha` method is used to check if a character is a letter, and the `isupper` method is used to check if a letter is uppercase. The `index` method is used to find the index of a character in a string. The `chr` function is used to convert an ASCII code back to a character. The `ord` function is used to convert a character to its ASCII code.  The `+ 32` is used to convert uppercase letters to lowercase, and the `- 32` is used to convert lowercase letters to uppercase. The `chr` function is used to convert the resulting code to a character. The `ord` function is used to convert the characters to their ASCII codes, and `chr` is used to convert the ASCII codes back to characters. The `isalpha` method is used to check if a character is a letter, and the `isupper` method is used to check if a letter is uppercase. The `index` method is used