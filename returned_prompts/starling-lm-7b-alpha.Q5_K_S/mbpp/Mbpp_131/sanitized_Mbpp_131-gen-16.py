def reverse_vowels(word):
    word_list = list(word)
    vowels = "aeiou"
    i, j = 0, len(word) - 1
    while i < j:
        if word_list[i] in vowels:
            while word_list[j] not in vowels:
                j -= 1
            word_list[i], word_list[j] = word_list[j], word_list[i]
            i += 1
        else:
            i += 1
    return ''.join(word_list)