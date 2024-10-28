    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'm', 'u': 'q', 'A': 'C', 'E': 'G', 'I': 'K', 'O': 'M', 'U': 'Q'}
    encoded_message = ""

    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded_message += vowels[char]
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += char

    return encoded_message


