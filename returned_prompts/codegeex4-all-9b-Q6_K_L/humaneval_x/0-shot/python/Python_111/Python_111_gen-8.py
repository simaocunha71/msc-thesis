def histogram(test):
    counts = {}
    if test == '':
        return counts
    for letter in test.split():
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    max_count = max(counts.values())
    most_frequent = {key: value for key, value in counts.items() if value == max_count}
    return most_frequent

print(histogram('a b c'))  # {'a': 1, 'b': 1, 'c': 1}
print(histogram('a b b a'))  # {'a': 2, 'b': 2}
print(histogram('a b c a b'))  # {'a': 2, 'b': 2}
print(histogram('b b b b a'))  # {'b': 4}
print(histogram(''))  # {}