    words = s.split()
    result = []
    for word in words:
        if len([letter for letter in word if letter not in "aeiou"]) == n:
            result.append(word)

    return result


