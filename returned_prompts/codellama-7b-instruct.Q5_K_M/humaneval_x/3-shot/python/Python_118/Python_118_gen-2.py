    vowels = ["a", "e", "i", "o", "u"]
    word = word.upper()
    for i in range(len(word) - 1, -1, -1):
        if word[i] in vowels:
            if i < len(word) - 1 and word[i + 1] not in vowels:
                return word[i]
            elif i > 0 and word[i - 1] not in vowels:
                return word[i]
            else:
                continue

    return ""


