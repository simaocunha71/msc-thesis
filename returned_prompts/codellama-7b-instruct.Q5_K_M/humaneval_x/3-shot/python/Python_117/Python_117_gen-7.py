    words = s.split()
    result = []
    for word in words:
        if len([x for x in word if x.lower() not in 'aeiou']) == n:
            result.append(word)

    return result


