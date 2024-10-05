```
def encode(message):
    result = ''
    for char in message:
        if char.isalpha():
            if char.lower() in 'aeiou':
                result += chr((ord(char.lower()) + 2 - 97) % 26 + 97)
            else:
                result += char.swapcase()
        else:
            result += char
    return result
```
This function iterates over each character in the message. If the character is a letter, it checks if it's a vowel. If it's a vowel, it replaces it with the letter that appears 2 places ahead of it in the alphabet. If it's not a vowel, it swaps the case of the letter. If the character is not a letter, it leaves it unchanged. The result is the encoded message. The `ord` function returns the ASCII value of a character, and the `chr` function returns the character represented by a specified ASCII value. The `% 26` is used to handle cases where the ASCII value of the character plus 2 exceeds the ASCII value of 'z'. The `swapcase` method swaps the case of the letter. The `isalpha` method checks if the character is a letter. The `lower` method returns the lowercase version of the character. The `in` operator checks if a string is a substring of another string. The `97` is the ASCII value of 'a'. The `ord` function returns the ASCII value of a character. The `chr` function returns the character represented by a specified ASCII value. The `% 26` is used to handle cases where the ASCII value of the character plus 2 exceeds the ASCII value of 'z'. The `swapcase` method swaps the case of the letter. The `isalpha` method checks if the character is a letter. The `lower` method returns the lowercase version of the character. The `in` operator checks if a string is a substring of another string. The `97` is the ASCII value of 'a'. The `ord` function returns the ASCII value of a character. The `chr` function returns the character represented by a specified ASCII value. The `% 26` is used to handle cases where the ASCII value of the character plus 2 exceeds the ASCII value of 'z'. The `swapcase` method swaps the case of the letter. The `isalpha` method checks if the character is a letter. The `lower` method returns the lowercase version of the character. The `in