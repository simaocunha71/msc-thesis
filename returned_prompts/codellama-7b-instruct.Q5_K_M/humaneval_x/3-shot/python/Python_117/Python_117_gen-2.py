    words = s.split()
    result = []
    for word in words:
        if len(word) == n and len([c for c in word if c.isalpha() and not c.isupper()]) == n:
            result.append(word)
    return result


