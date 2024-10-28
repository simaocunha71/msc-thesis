    words = s.split()
    result = []

    for word in words:
        vowels = ["a", "e", "i", "o", "u"]
        consonants = [c for c in word if c not in vowels]

        if len(consonants) == n:
            result.append(word)

    return result


