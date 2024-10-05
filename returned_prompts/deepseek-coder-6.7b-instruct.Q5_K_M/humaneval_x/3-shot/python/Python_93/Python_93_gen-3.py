    vowels = 'aeiou'
    encoded_message = ''

    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded_character = chr((ord(char) + 2) % 26 + ord('a'))
                encoded_message += encoded_character if char.islower() else encoded_character.upper()
            else:
                encoded_message += char.lower() if char.isupper() else char.upper()
        else:
            encoded_message += char

    return encoded_message


