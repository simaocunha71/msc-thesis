    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'm', 'u': 'q', 'A': 'C', 'E': 'G', 'I': 'K', 'O':': 'M', 'U': 'Q'}
    encoded = ''
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                encoded += vowels[letter]
            else:
                encoded += letter.swapcase()
        else:
            encoded += letter
    return encoded


