    result = []
    vowels = 'aeiou'

    for word in s.split():
        consonants = sum(1 for c in word if c.lower() not in vowels)
        if consonants == n:
            result.append(word)

    return result

