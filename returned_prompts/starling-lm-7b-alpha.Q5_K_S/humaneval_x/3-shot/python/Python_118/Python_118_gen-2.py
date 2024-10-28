    vowels = "aeiou"
    for idx, char in enumerate(word):
        if char in vowels and idx != 0 and idx != len(word) - 1:
            return char

    return ""


