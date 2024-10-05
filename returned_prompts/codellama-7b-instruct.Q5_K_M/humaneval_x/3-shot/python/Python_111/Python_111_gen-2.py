    histogram = {}
    for letter in test:
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram[letter] = 1

    return histogram


