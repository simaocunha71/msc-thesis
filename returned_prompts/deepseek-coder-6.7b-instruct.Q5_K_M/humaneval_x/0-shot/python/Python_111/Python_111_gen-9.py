
    def histogram(test):
        letter_count = {}
        for letter in test.split():
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1
                
        max_count = max(letter_count.values()) if letter_count else 0
        return {k: v for k, v in letter_count.items() if v == max_count}

    return histogram(test)


print(histogram('a b c'))  # {'a': 1, 'b': 1, 'c': 1}
print(histogram('a b b a'))  # {'a': 2, 'b': 2}
print(histogram('a b c a b'))  # {'a': 2, 'b': 2}
print(histogram('b b b b a'))  # {'b': 4}
print(histogram(''))  # {}


