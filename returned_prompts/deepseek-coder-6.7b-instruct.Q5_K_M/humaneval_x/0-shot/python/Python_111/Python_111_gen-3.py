
    def histogram(test):
        letter_counts = {}
        for letter in test.split():
            if letter not in letter_counts:
                letter_counts[letter] = 1
            else:
                letter_counts[letter] += 1
        max_count = max(letter_counts.values()) if letter_counts else 0
        return {letter: count for letter, count in letter_counts.items() if count == max_count}

    print(histogram('a b c'))  # {'a': 1, 'b': 1, 'c': 1}
    print(histogram('a b b a'))  # {'a': 2, 'b': 2}
    print(histogram('a b c a b'))  # {'a': 2, 'b': 2}
    print(histogram('b b b b a'))  # {'b': 4}
    print(histogram(''))  # {}



