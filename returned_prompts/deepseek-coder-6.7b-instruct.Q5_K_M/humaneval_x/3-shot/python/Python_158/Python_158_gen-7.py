    max_unique = 0
    max_word = ""

    for word in words:
        num_unique = len(set(word))
        if num_unique > max_unique:
            max_unique = num_unique
            max_word = word
        elif num_unique == max_unique:
            max_word = min(word, max_word)

    return max_word


