    consonants = 'bcdfghjklmnpqrstvwxyz'
    result = []
    words = s.split()

    for word in words:
        count = 0
        for char in word:
            if char.lower() in consonants:
                count += 1

        if count == n:
            result.append(word)

    return result