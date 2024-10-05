```
def encode(message):
    vowels = 'aeiouAEIOU'
    result = []
    for char in message:
        if char in vowels:
            if char.islower():
                result.append(chr((ord(char) - ord('a') + 2) % 26 + ord('a')))
            else:
                result.append(chr((ord(char) - ord('A') + 2) % 26 + ord('A')))
        elif char.isalpha():
            if char.islower():
                result.append(chr((ord(char) - ord('a')) + ord('A')))
            else:
                result.append(chr((ord(char) - ord('A')) + ord('a')))
        else:
            result.append(char)
    return ''.join(result)
```


The given function works as follows:
- It iterates over each character in the input message.
- If the character is a vowel (either lowercase or uppercase), it replaces the vowel with the letter that appears 2 places ahead in the English alphabet. It handles this by subtracting the ASCII value of 'a' or 'A' from the ASCII value of the vowel, adding 2, taking the modulus with 26 to ensure the result is within the range of lowercase or uppercase letters, and then adding the ASCII value of 'a' or 'A' back to get the ASCII value of the new letter.
- If the character is a letter but not a vowel, it swaps the case of the letter by subtracting the ASCII value of 'a' or 'A' from the ASCII value of the letter, adding the ASCII value of the opposite case letter ('A' for lowercase, 'a' for uppercase), and then converting the result back to a character.
- If the character is not a letter, it simply adds the character to the result as is.
- Finally, it joins all the characters in the result list into a single string and returns it.