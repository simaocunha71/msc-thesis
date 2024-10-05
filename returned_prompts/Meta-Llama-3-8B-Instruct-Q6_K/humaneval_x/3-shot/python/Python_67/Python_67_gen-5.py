    words = s.split()
    n_apples = 0
    for i in range(len(words)):
        if words[i].endswith('apples'):
            n_apples = int(words[i-1])

    return n - n_apples - int(s.split()[-1].replace('oranges', ''))


