    import collections

    hist = collections.defaultdict(int)
    for letter in test:
        hist[letter] += 1

    return hist


