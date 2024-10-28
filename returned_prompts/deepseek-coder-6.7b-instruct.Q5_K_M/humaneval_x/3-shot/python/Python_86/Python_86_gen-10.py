    words = s.split(' ')
    return ' '.join(sorted(words, key=lambda w: [ord(c) for c in w]))


