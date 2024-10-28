    # Swap all case
    message = message.swapcase()

    # Replace vowels
    message = message.replace('A', 'Z')
    message = message.replace('E', 'D')
    message = message.replace('I', 'C')
    message = message.replace('O', 'B')
    message = message.replace('U', 'A')
    message = message.replace('Y', 'X')

    return message


