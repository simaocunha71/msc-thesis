
def histogram(test):
    histogram = {}
    for letter in test:
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram[letter] = 1
    return histogram

# print(histogram('a b c')) # {'a': 1, 'b': 1, 'c': 1}
# print(histogram('a b b a')) # {'a': 2, 'b': 2}
# print(histogram('a b c a b')) # {'a': 2, 'b': 2}
# print(histogram('b b b b a')) # {'b': 4}
# print(histogram('')) # {}


# Given a string representing a space separated lowercase letters, return a dictionary of the letter with the most repetition and containing the corresponding count. If several letters have the same occurrence, return all of them.

def histogram(test):
    histogram = {}
    for letter in test.split():
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram[letter] = 1
    return histogram

# print(histogram('a b c')) # {'a': 1, 'b': 1, 'c': 1}
# print(histogram('a b b a')) # {'a': 2, 'b': 2}
# print(histogram('a b c a b')) # {'a': 2, 'b': 2}
# print(histogram('b b b b a')) # {'b': 4}
# print(histogram('')) # {}


def histogram(test):
    histogram = {}
    for letter in test:
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram[letter] = 1
    return histogram

# print(histogram('a b c')) # {'a': 1, 'b': 1, 'c': 1}
# print(histogram('a b b a')) # {'a': 2, 'b': 2}
# print(histogram('a b c