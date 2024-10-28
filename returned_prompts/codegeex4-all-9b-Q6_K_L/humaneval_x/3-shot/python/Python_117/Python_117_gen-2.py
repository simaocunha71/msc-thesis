    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    words = s.split()
    result = []

    for word in words:
        consonants = sum(1 for c in word if c.lower() not in vowels)
        if consonants == n:
            result.append(word)

    return result

