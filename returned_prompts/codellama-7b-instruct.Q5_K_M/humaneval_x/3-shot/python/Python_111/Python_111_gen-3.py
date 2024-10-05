    histogram = {}
    for letter in test:
        if letter not in histogram:
            histogram[letter] = 1
        else:
            histogram[letter] += 1
    return histogram


