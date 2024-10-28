    vowels = 'aeiouAEIOU'
    encoded_message = ''
    
    for char in message:
        if char in vowels:
            if char.islower():
                encoded_message += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
            else:
                encoded_message += chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
        elif char.isalpha():
            if char.islower():
                encoded_message += chr((ord(char) - ord('a')) % 26 + ord('a'))
            else:
                encoded_message += chr((ord(char) - ord('A')) % 26 + ord('A'))
        else:
            encoded_message += char
    
    return encoded_message


