    vowels = 'aeiouAEIOU'
    word = list(word)
    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels:
            for j in range(i - 1, -1, -1):
                if word[j] in vowels:
                    return word[j]
                if word[j] not in vowels:
                    break
    return ""


