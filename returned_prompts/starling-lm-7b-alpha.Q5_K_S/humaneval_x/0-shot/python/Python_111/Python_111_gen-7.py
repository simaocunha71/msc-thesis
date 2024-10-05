
def histogram(test):
    histo = {}
    for char in test:
        if char in histo:
            histo[char] += 1
        else:
            histo[char] = 1
    max_key = max(histo, key=histo.get)
    max_value = histo[max_key]
    res = {}
    for key, value in histo.items():
        if value == max_value:
            res[key] = value
    return res


#print(histogram('a b c'))  # {'a': 1, 'b': 1, 'c': 1}
#print(histogram('a b b a'))  # {'a': 2, 'b': 2}
#print(histogram('a b c a b'))  # {'a': 2, 'b': 2}
#print(histogram('b b b b a'))  # {'b': 4}
#print(histogram(''))  # {}


def histogram(test):
    histo = {}
    for char in test:
        if char in histo:
            histo[char] += 1
        else:
            histo[char] = 1
    max_key = max(histo, key=histo.get)
    max_value = histo[max_key]
    res = {}
    for key, value in histo.items():
        if value == max_value:
            res[key] = value
    return res

#print(histogram('a b c'))  # {'a': 1, 'b': 1, 'c': 1}
#print(histogram('a b b a'))  # {'a': 2, 'b': 2}
#print(histogram('a b c a b'))  # {'a': 2, 'b': 2}
#print(histogram('b b b b a'))  # {'b': 4}
#print(histogram(''))  # {}




def histogram(test):
    histo = {}
    for char in test:
        if char in histo:
