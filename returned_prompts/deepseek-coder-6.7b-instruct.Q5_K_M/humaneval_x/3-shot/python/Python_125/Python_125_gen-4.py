    words = txt.split()
    if len(words) > 1:
        return words
    words = txt.split(',')
    if len(words) > 1:
        return words
    return sum(1 for c in txt if c.islower()) % 2


