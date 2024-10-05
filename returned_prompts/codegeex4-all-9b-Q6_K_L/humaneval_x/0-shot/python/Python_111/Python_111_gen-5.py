def histogram(test):
    test_list = test.split()
    # create a dictionary with the letters as keys and their count as values
    letter_count = {letter: test_list.count(letter) for letter in test_list}
    # find the maximum count
    max_count = max(letter_count.values())
    # find the letters with the maximum count
    max_letters = [letter for letter, count in letter_count.items() if count == max_count]
    # return the dictionary with the letters and their count
    return {letter: max_count for letter in max_letters}

print(histogram('a b c'))  # {'a': 1, 'b': 1, 'c': 1}
print(histogram('a b b a'))  # {'a': 2, 'b': 2}
print(histogram('a b c a b'))  # {'a': 2, 'b': 2}
print(histogram('b b b b a'))  # {'b': 4}
print(histogram(''))  # {}