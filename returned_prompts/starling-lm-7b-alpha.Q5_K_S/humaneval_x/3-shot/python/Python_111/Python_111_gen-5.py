    histo = {}

    for char in test:
        if char in histo:
            histo[char] += 1
        else:
            histo[char] = 1

    return histo


