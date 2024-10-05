    vowels = "aeiou"
    result = []
    words = s.split()

    for word in words:
        consonants = sum(1 for c in word if c.lower() not in vowels)
        if consonants == n:
            result.append(word)

    return result

