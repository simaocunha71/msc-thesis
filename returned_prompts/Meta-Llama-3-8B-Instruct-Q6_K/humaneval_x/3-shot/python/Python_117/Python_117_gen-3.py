    vowels = 'aeiouAEIOU'
    words = s.split()
    result = []

    for word in words:
        consonants = 0
        for char in word:
            if char.isalpha() and char not in vowels:
                consonants += 1
        if consonants == n:
            result.append(word)

    return result


