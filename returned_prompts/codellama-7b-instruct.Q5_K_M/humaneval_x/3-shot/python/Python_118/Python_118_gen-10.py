    vowels = ['A', 'E', 'I', 'O', 'U']
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            if word[i+1] in consonants:
                return word[i]

    return ''


