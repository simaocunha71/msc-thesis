    # Convert all the characters to uppercase
    message = message.upper()
    encoded_message = ''
    # Iterate through all the characters in the message
    for idx, char in enumerate(message):
        # If the character is not a letter, leave it as it is
        if char.isalpha():
            # If the character is a vowel
            if char in 'AEIOU':
                # Replace the character with the character that is 2 places ahead
                encoded_message += ' ' + message[idx + 2]
            # Otherwise just leave it as it is
            else:
                encoded_message += char

    # Remove all the spaces
    encoded_message = encoded_message.replace(' ', '')
    return encoded_message


