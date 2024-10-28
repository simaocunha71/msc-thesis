    consonants = "bcdfghjklmnpqrstvwxyz"
    words = s.split()
    result = []
    for word in words:
        count = sum(1 for c in word if c.lower() in consonants)
        if count == n:
            result.append(word)
    return result

