    vowels = "aeiou"
    VOWELS = "AEIOU"
    encoded = ''
    for char in message:
        if char in vowels:
            encoded += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        elif char in VOWELS:
            encoded += chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
        else:
            encoded += char
    return encoded


