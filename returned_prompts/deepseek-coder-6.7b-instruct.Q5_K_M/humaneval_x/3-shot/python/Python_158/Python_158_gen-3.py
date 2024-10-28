    max_unique = 0
    max_word = ''
    for word in words:
        num_unique = len(set(word))
        if num_unique > max_unique or (num_unique == max_unique and word < max_word):
            max_unique = num_unique
            max_word = word
    return max_word


