    vowels = 'aeiouAEIOU'
    encoded_message = ''
    
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                if char.isupper():
                    encoded_message += chr(ord(char) + 2).upper()
                else:
                    encoded_message += chr(ord(char) + 2).lower()
            else:
                if char.isupper():
                    encoded_message += char.lower()
                else:
                    encoded_message += char.upper()
        else:
            encoded_message += char
    
    return encoded_message

