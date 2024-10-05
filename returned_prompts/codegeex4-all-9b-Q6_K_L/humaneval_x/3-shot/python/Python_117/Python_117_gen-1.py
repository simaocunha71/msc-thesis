    vowels = "aeiou"
    result = []
    for word in s.split():
        consonants = sum(c.lower() not in vowels for c in word)
        if consonants == n:
            result.append(word)
    return result

