    vowels = 'aeiouAEIOU'
    for i in range(1, len(word) - 1):
        if word[i] in vowels:
            return word[i]
        if word[i - 1] in vowels and word[i + 1] in vowels:
            return word[i]
    return ''


