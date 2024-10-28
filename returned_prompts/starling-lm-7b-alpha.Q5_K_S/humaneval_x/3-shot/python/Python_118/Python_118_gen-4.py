    vowels = "AEIOUaeiou"
    for idx, char in enumerate(word):
        if char not in vowels:
            if idx < len(word) - 1 and word[idx + 1] in vowels:
                return word[idx + 1]
            if idx > 0 and word[idx - 1] in vowels:
                return word[idx - 1]
    return ""


