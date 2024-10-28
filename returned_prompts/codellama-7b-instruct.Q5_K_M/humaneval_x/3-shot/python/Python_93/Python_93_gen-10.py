    message = message.upper()
    encoded_message = ""
    for i, char in enumerate(message):
        if char in "AEIOU":
            encoded_message += chr((ord(char) + 2) % 26 + ord('A'))
        else:
            encoded_message += char
    return encoded_message

