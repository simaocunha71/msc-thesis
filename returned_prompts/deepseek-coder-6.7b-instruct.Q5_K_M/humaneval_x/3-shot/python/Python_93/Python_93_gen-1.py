    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.lower() in 'aeiou':
                encoded_message += chr(ord(char)+2) if char.islower() else chr(ord(char)+2).upper()
            else:
                encoded_message += chr(ord(char)^32) if char.islower() else chr(ord(char)^32).upper()
        else:
            encoded_message += char
    return encoded_message

The encode function works by iterating through each character in the message. If the character is a letter, it checks if it is a vowel. If it is, it adds 2 to the ASCII value of the character (using the ord and chr functions), wrapping around to the beginning of the alphabet if necessary. If it is not a vowel, it simply swaps the case of the character. If the character is not a letter, it adds it to the encoded message as is.

Note: The ^ operator in Python is the bitwise XOR operator. The integer 32 represents the difference in ASCII values between uppercase and lowercase letters.

