    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ""

    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded_message += chr((ord(char) - 97 + 2) % 26 + 97).upper() if char.isupper() else chr((ord(char) - 97 + 2) % 26 + 97).lower()
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += char

    return encoded_message

