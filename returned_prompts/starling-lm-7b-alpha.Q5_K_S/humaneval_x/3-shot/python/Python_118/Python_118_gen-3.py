    vowels = "aeiou"
    for idx in range(len(word) - 2, -1, -1):
        if word[idx] in vowels:
            return word[idx]
        if word[idx + 1] in vowels:
            return word[idx + 1]
    return ""


