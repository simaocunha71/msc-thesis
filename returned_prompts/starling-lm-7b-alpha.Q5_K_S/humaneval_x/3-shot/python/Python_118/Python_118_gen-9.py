    vowels = "aeiou"
    for idx, char in enumerate(word):
        if char.lower() in vowels:
            if idx > 0 and word[idx - 1].isalpha():
                if idx < len(word) - 1 and word[idx + 1].isalpha():
                    return char
    return ""


