
def histogram(test):
    letter_count = {}
    for letter in test:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    max_count = max(letter_count.values())
    for letter in letter_count:
        if letter_count[letter] == max_count:
            yield (letter, max_count)

# test code to run 
# print(list(histogram('a b c')))
# print(list(histogram('a b b a')))
# print(list(histogram('a b c a b')))
# print(list(histogram('b b b b a')))
# print(list(histogram('')))
