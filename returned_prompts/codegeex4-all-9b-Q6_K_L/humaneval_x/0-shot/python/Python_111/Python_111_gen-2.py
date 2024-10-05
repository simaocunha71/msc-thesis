def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    if test == '':
        return {}
    else:
        freq = {}
        for letter in test.split():
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
        max_freq = max(freq.values())
        return {k: v for k, v in freq.items() if v == max_freq}

print(histogram('a b c')) # {'a': 1, 'b': 1, 'c': 1}
print(histogram('a b b a')) # {'a': 2, 'b': 2}
print(histogram('a b c a b')) # {'a': 2, 'b': 2}
print(histogram('b b b b a')) # {'b': 4}
print(histogram('')) # {}