    vowels = ["a", "e", "i", "o", "u"]
    if len(word) < 3:
        return ""
    for i in range(1, len(word)-1):
        if word[i] in vowels:
            return word[i]
        if word[i-1] not in vowels and word[i+1] not in vowels:
            return ""
    return ""


