    vowels = "aeiouAEIOU"
    for i in range(len(word) - 2, -1, -1):
        if word[i] in vowels:
            return word[i]
        if word[i + 1] in vowels:
            return word[i + 1]
    return ""


