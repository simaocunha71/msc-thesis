    vowels = 'AEIOUaeiou'
    word = word.lstrip()  # Remove leading vowels
    word = word.rstrip()  # Remove trailing vowels

    for i in range(len(word) - 1, -1, -1):
        if word[i] in vowels:
            return word[i]
    return ''


