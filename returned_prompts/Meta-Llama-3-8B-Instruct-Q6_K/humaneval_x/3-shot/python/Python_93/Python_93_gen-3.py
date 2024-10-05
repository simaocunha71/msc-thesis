    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char in vowels:
            index = vowels.index(char)
            encoded_message += chr(ord(vowels[index]) + 2)
        elif char.isalpha():
            if char.islower():
                encoded_message += chr(ord(char) + 32)
            else:
                encoded_message += chr(ord(char) - 32)
        else:
            encoded_message += char
    return encoded_message


