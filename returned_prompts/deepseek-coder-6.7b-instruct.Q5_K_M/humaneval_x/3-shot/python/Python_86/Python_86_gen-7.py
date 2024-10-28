    words = s.split(' ')
    ordered_words = [''.join(sorted(w)) for w in words]
    return ' '.join(ordered_words)


