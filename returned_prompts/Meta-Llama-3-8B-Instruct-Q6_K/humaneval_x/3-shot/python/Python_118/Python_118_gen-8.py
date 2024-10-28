    vowels = 'aeiouAEIOU'
    word = word[::-1]
    for i, char in enumerate(word):
        if char in vowels:
            if i < len(word) - 1 and word[i + 1] not in vowels:
                return char
    return ''


