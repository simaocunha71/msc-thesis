```
def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char in vowels:
            if char.islower():
                encoded_message += chr(ord(char) + 2)
            else:
                encoded_message += chr(ord(char) - 22)
        elif char.isalpha():
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
        else:
            encoded_message += char
    return encoded_message
```


The function `encode` takes a message as an argument and returns the encoded message. It iterates over each character in the message. If the character is a vowel, it moves it 2 places ahead in the alphabet. If the character is not a vowel and is a letter, it swaps its case. If the character is not a letter, it leaves it as it is. The function uses the `ord` function to get the ASCII value of a character, and the `chr` function to get the character represented by a specific ASCII value. The `islower` and `isupper` methods are used to check if a character is lowercase or uppercase. The `chr(ord(char) + 2)` expression moves a lowercase vowel 2 places ahead in the alphabet, and the `chr(ord(char) - 22)` expression moves an uppercase vowel 2 places ahead in the alphabet. The `chr(ord(char) + 2)` expression moves a lowercase vowel 2 places ahead in the alphabet, and the `chr(ord(char) - 22)` expression moves an uppercase vowel 2 places ahead in the alphabet. The `chr(ord(char) - 22)` expression moves an uppercase vowel 2 places ahead in the alphabet. The `chr(ord(char) + 2)` expression moves a lowercase vowel 2 places ahead in the alphabet. The `chr(ord(char) - 22)` expression moves an uppercase vowel 2 places ahead in the alphabet. The `chr(ord(char) + 2)` expression moves a lowercase vowel 2 places ahead in the alphabet, and the `chr(ord(char) - 22)` expression moves an uppercase vowel 2 places ahead in the alphabet. The `chr(ord(char) + 2)` expression moves a lowercase vowel 2 places ahead in the alphabet, and the `chr(ord(char) - 22)` expression moves an uppercase vowel 2 places ahead in the alphabet. The `chr(ord(char) + 2)`