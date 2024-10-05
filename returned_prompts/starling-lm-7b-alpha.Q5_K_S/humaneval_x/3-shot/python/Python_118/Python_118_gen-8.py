    vowels = "aeiou"
    for idx in range(1, len(word)-1):
        if word[idx] in vowels:
            return word[idx]

    return ""


