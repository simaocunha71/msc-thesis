    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(word)-2, -1, -1):
        if word[i] in vowels and word[i+2] in vowels:
            return word[i+1]
    return ''