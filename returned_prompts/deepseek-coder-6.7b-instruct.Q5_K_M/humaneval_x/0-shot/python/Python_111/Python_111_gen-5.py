
    def histogram(test):
        letter_frequency = {}
        for letter in test.split():
            if letter not in letter_frequency:
                letter_frequency[letter] = 1
            else:
                letter_frequency[letter] += 1
        max_frequency = max(letter_frequency.values())
        return {k: v for k, v in letter_frequency.items() if v == max_frequency}

    print(histogram('a b c'))  # == {'a': 1, 'b': 1, 'c': 1}
    print(histogram('a b b a'))  # == {'a': 2, 'b': 2}
    print(histogram('a b c a b'))  # == {'a': 2, 'b': 2}
    print(histogram('b b b b a'))  # == {'b': 4}
    print(histogram(''))  # == {}


In the function histogram, we first initialize an empty dictionary letter_frequency. Then, for each letter in the input string, we either add it to the dictionary if it's not there yet, or increment its count if it is there.

After that, we find the maximum frequency of any letter in the dictionary. We then return a new dictionary containing only the entries whose value (frequency) is equal to this maximum.



"""



def histogram(test):
    letter_frequency = {}
    for letter in test.split():
        if letter not in letter_frequency:
            letter_frequency[letter] = 1
        else:
            letter_frequency[letter] += 1
    max_frequency = max(letter_frequency.values())
    return {k: v for k, v in letter_frequency.items() if v == max_frequency}


print(histogram('a b c'))  # == {'a': 1, 'b': 1, 'c': 1}
print(histogram('a b b a'))  # == {'a': 2, 'b': 2}
print(histogram('a b c a b'))  # == {'a': 2, 'b': 2}
print(histogram('b b b b a'))