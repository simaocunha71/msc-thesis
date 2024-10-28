def remove_length(s, k):
    words = s.split(' ')
    new_words = []
    for word in words:
        if len(word) != k:
            new_words.append(word)
    return ' '.join(new_words)