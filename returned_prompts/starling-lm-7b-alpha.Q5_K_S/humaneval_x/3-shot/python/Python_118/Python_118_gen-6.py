    vowel = "AEIOU"
    for i in range(1, len(word)-1):
        if word[i] in vowel:
            return word[i]

    return ""


