    vowels = 'aeiouAEIOU'
    for i in range(len(word) - 1, 1, -1):
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            return word[i]
    return ''