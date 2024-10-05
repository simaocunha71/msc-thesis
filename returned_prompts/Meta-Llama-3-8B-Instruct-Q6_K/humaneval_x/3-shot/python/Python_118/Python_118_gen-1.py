    vowels = 'aeiouAEIOU'
    word = list(word)
    for i in range(len(word) - 2, -1, -1):
        if word[i] in vowels:
            return chr(word[i])

    return ''
