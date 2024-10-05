    def is_consonant(c):
        return c not in "aeiou"

    vowels = "aeiou"
    result = []
    word = ""
    for c in s:
        if c in vowels:
            if len(word) == n:
                if not any(c not in vowels for c in word):
                    result.append(word)
                word = ""
        else:
            word += c
    if len(word) == n:
        if not any(c not in vowels for c in word):
            result.append(word)

    return result


