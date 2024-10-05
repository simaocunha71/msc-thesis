    vowels = "AEIOUaeiou"
    for idx in range(len(word) - 2, 0, -1):
        if word[idx] in vowels and word[idx-1] not in vowels and word[idx+1] not in vowels:
            return word[idx]
    return ""


