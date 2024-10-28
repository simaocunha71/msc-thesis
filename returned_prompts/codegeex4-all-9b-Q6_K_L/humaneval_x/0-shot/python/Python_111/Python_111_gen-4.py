def histogram(test):
    from collections import Counter

    result = Counter(test.split())
    if not result:
        return {}

    max_value = max(result.values())
    return {k: v for k, v in result.items() if v == max_value}

print(histogram('a b c'))  # {'a': 1, 'b': 1, 'c': 1}
print(histogram('a b b a'))  # {'a': 2, 'b': 2}
print(histogram('a b c a b'))  # {'a': 2, 'b': 2}
print(histogram('b b b b a'))  # {'b': 4}
print(histogram(''))  # {}



