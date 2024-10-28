    words = s.split()
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

    result = []

    for word in words:
        if len(word) == n and all(letter in consonants for letter in word):
            result.append(word)

    return result


