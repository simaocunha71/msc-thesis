    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    words = s.split()
    result = []

    for word in words:
        count = 0
        for c in word:
            if c in consonants:
                count += 1
        if count == n:
            result.append(word)

    return result

