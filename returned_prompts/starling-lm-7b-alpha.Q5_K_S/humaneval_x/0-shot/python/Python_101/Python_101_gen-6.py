
def words_string(s):
    words = []
    for word in s.split(','):
        words.append(word.strip())
    return words

# print(words_string("Hi, my name is John"))
# print(words_string("One, two, three, four, five, six"))

