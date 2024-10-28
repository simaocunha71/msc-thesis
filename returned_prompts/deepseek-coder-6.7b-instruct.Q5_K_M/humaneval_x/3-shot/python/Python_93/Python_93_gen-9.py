    vowels = 'aeiou'
    encoded = ''
    for char in message:
        if char.isalpha():
            if char.isupper():
                encoded += char.lower()
            else:
                encoded += char.upper()
        else:
            encoded += char
        if char.lower() in vowels:
            encoded = encoded[:-1] + chr((ord(char) - 97 + 2) % 26 + 97) + encoded[-1:]
    return encoded


