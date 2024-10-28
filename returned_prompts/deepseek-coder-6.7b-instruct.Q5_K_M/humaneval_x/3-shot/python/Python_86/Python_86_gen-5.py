    words = s.split(' ')
    for i, word in enumerate(words):
        sorted_word = ''.join(sorted(word))
        words[i] = sorted_word
    return ' '.join(words)


