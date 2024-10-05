    histogram = {}
    for letter in test.split():
        histogram[letter] = histogram.get(letter, 0) + 1
    max_val = max(histogram.values()) if histogram else 0
    return {k: v for k, v in histogram.items() if v == max_val}


